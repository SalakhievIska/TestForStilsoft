<template>
  <div>
    <v-toolbar flat class="px-10">
      <v-toolbar-title>
        <div class="text-h5 font-weight-bold">
          Секции
        </div>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn
          rounded
          depressed
          color="purple lighten-2"
          dark
          @click="addSection">
        <v-icon>fas fa-plus</v-icon>
        <span class="ml-2">Добавить секцию</span>
      </v-btn>
    </v-toolbar>

    <v-divider>
    </v-divider>

    <v-row>
      <v-col cols="2" class="elevation-1">
        <v-form
            ref="filterForm"
            class="px-4 my-5">
          <v-text-field
              v-model="filterForm.name"
              label="Название">
          </v-text-field>

          <v-btn color="grey lighten-2" @click="resetFilterForm">
            <v-icon small class="mx-1">
              fas fa-times
            </v-icon>
            Сбросить
          </v-btn>

          <v-btn color="purple lighten-2 ml-2" dark @click="filter">
            <v-icon small class="mx-1">
              fas fa-filter
            </v-icon>
            Фильтр
          </v-btn>
        </v-form>
      </v-col>

      <v-col cols="10">
        <v-data-table
            :headers="headers"
            :items="tableData"
            class="px-10 my-5"
            locale="ru-ru"
            hide-default-footer>

          <template v-slot:item.actions="{ item }">
            <v-icon
                small
                class="mr-2"
                @click="addStudent(item.id)">
              fas fa-user-plus
            </v-icon>
            <v-icon
                small
                class="mr-2"
                @click="editSection(item.id)">
              fas fa-edit
            </v-icon>
            <v-icon
                small
                @click="deleteSection(item.id)">
              fas fa-trash-alt
            </v-icon>
          </template>

          <template v-slot:item.students="{ item }">
            <span v-for="student in item.students" :key="student.key">
              {{ student.text }}
              <v-icon
                  small
                  class="ml-2"
                  @click="deleteStudentInSection(student.key)">
                fas fa-trash-alt
              </v-icon>
              <br>
            </span>
          </template>

          <template v-slot:no-data>
            Список секицй пуст!
          </template>
        </v-data-table>

        <Paginator
            v-on:update-pagination="updatePagination($event)"
            :num-pages="numPages"/>
      </v-col>
    </v-row>

    <v-dialog
        v-model="sectionAddEditDialog"
        max-width="600">
      <SectionAddEdit
          :section-id="sectionIdForEdit"
          v-on:section-add="sectionAdd($event)"
          v-on:section-edit="sectionEdit($event)"
          v-on:close-dialog="closeDialog"/>
    </v-dialog>

    <v-dialog
        v-model="sectionDeleteDialog"
        max-width="400">
      <SectionDelete
          :section-id="sectionIdForDelete"
          v-on:section-delete="sectionDelete($event)"
          v-on:close-dialog="closeDialog"/>
    </v-dialog>

    <v-dialog
        v-model="studentInSectionAddDialog"
        max-width="500">
      <StudentInSectionAdd
          :section-id="sectionIdForStudentInSectionAdd"
          v-on:section-edit="sectionEdit($event)"
          v-on:close-dialog="closeDialog"/>
    </v-dialog>

    <v-dialog
        v-model="studentInSectionDeleteDialog"
        max-width="450">
      <StudentInSectionDelete
          :student-in-section-id="studentInSectionIdForDelete"
          v-on:section-edit="sectionEdit($event)"
          v-on:close-dialog="closeDialog"/>
    </v-dialog>
  </div>
</template>

<script>
import api from '/src/apis/api';
import moment from 'moment';
import _ from 'lodash';
import SectionAddEdit from '/src/Components/Sections/SectionAddEdit';
import SectionDelete from '/src/Components/Sections/SectionDelete';
import StudentInSectionAdd from '/src/Components/Sections/StudentInSectionAdd';
import StudentInSectionDelete from '/src/Components/Sections/StudentInSectionDelete';
import Paginator from '/src/Components/Utils/Paginator.vue';
import withPagination from '/src/Components/Utils/paginator.js';

export default {
  name: 'Sections',

  components: {
    SectionAddEdit, SectionDelete, StudentInSectionAdd, StudentInSectionDelete, Paginator,
  },

  data: () => ({
    headers: [
      { text: '№', value: 'id' },
      { text: 'Название', value: 'name' },
      { text: 'Количество студентов', value: 'studentCount' },
      { text: 'Студенты', value: 'students' },
      { text: 'Действия', value: 'actions', align: 'end' },
    ],
    tableData: [],
    pageSize: 10,
    page: 1,
    numPages: 1,

    filterForm: {},

    sectionAddEditDialog: false,
    sectionDeleteDialog: false,
    studentInSectionAddDialog: false,
    studentInSectionDeleteDialog: false,

    sectionIdForEdit: 0,
    sectionIdForDelete: 0,
    sectionIdForStudentInSectionAdd: 0,
    studentInSectionIdForDelete: 0,
  }),

  computed: {
    emptyFilterForm: () => ({ name: '' }),
  },

  methods: {
    addSection() {
      this.sectionAddEditDialog = true;
      this.sectionIdForEdit = 0;
    },

    editSection(sectionId) {
      this.sectionIdForEdit = sectionId;
      this.sectionAddEditDialog = true;
    },

    deleteSection(sectionId) {
      this.sectionIdForDelete = sectionId;
      this.sectionDeleteDialog = true;
    },

    addStudent(sectionId) {
      this.sectionIdForStudentInSectionAdd = sectionId;
      this.studentInSectionAddDialog = true;
    },

    deleteStudentInSection(studentInSectionId) {
      this.studentInSectionIdForDelete = studentInSectionId;
      this.studentInSectionDeleteDialog = true;
    },

    formatSection: (section) => ({
      id: section.id,
      name: section.name,
      studentCount: section.studentCount,
      students: section.students.map((item) => ({
        text: `
          ${item.student.lastName} ${item.student.firstName} 
          с ${moment(item.joinDate).format('DD.MM.YYYY')}
        `,
        key: item.id,
      })),
    }),

    getSections() {
      withPagination(api.get('sections/', {
        params: {
          expand: 'students,students.student',
          ...this.filterForm,
          pageSize: this.pageSize,
          page: this.page,
        },
      })).then((response) => {
        this.numPages = response.paginator.numPages;
        this.tableData = _.map(response.data, (item) => this.formatSection(item));
      });
    },

    afterEditSections() {
      this.sectionAddEditDialog = false;
      this.sectionDeleteDialog = false;
      this.studentInSectionAddDialog = false;
      this.studentInSectionDeleteDialog = false;

      this.sectionIdForEdit = 0;
      this.sectionIdForDelete = 0;
      this.sectionIdForStudentInSectionAdd = 0;
      this.studentInSectionIdForDelete = 0;
    },

    filter() {
      this.getSections();
    },

    resetFilterForm() {
      this.$refs.filterForm.reset();
      this.getSections();
    },

    updatePagination(data) {
      this.page = data.page;
      this.pageSize = data.pageSize;
      this.getSections();
    },

    sectionAdd(section) {
      this.tableData = _.concat(this.tableData, this.formatSection(section));
      this.afterEditSections();
    },

    sectionEdit(section) {
      const sectionIndex = _.findIndex(this.tableData, (el) => el.id === section.id);
      this.tableData.splice(sectionIndex, 1, this.formatSection(section));
      this.afterEditSections();
    },

    sectionDelete(sectionId) {
      this.tableData = _.remove(this.tableData, (el) => el.id !== sectionId);
      this.afterEditSections();
    },

    closeDialog() {
      this.afterEditSections();
    },
  },

  created() {
    this.filterForm = this.emptyFilterForm;
    this.getSections();
  },
};

</script>
