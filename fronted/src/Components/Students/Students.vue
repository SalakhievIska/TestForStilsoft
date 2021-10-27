<template>
  <div>
    <v-toolbar flat class="px-10">
      <v-toolbar-title>Студенты</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
          rounded
          depressed
          color="purple lighten-2"
          dark
          @click="addStudent">
        <v-icon>fas fa-plus</v-icon>
        <span class="ml-2">Добавить студента</span>
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
              v-model="filterForm.firstName"
              label="Имя">
          </v-text-field>
          <v-text-field
              v-model="filterForm.lastName"
              label="Фамилия">
          </v-text-field>

          <v-radio-group
              v-model="filterForm.sex"
              row>
            <v-radio
                v-for="item in sex"
                :key="item.type"
                :label="item.text"
                :value="item.type">
            </v-radio>
          </v-radio-group>

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

          <template v-slot:item.profilePhotoUrl="{ item }">
            <v-avatar>
              <img v-if="item.profilePhotoUrl" :src="item.profilePhotoUrl">
              <v-icon v-else small>
                fas fa-user
              </v-icon>
            </v-avatar>
          </template>

          <template v-slot:item.isReadyToJoinToSection="{ item }">
            <v-icon
                color="green"
                small
                v-if="item.isReadyToJoinToSection">
              fas fa-check
            </v-icon>
            <v-icon
                color="red"
                small
                v-else>
              fas fa-times
            </v-icon>
          </template>

          <template v-slot:item.isCitizenOfRf="{ item }">
            <v-icon
                color="green"
                small
                v-if="item.isCitizenOfRf">
              fas fa-check
            </v-icon>
            <v-icon
                color="red"
                small
                v-else>
              fas fa-times
            </v-icon>
          </template>

          <template v-slot:item.actions="{ item }">
            <v-icon
                small
                class="mr-2"
                @click="editStudent(item.id)">
              fas fa-edit
            </v-icon>
            <v-icon
                small
                @click="deleteStudent(item.id)">
              fas fa-trash-alt
            </v-icon>
          </template>

          <template v-slot:item.sections="{ item }">
            <span v-for="section in item.sections" :key="section.id">
              {{ section.section.name }}
              <br>
            </span>
          </template>

          <template v-slot:no-data>
            Список студентов пуст!
          </template>
        </v-data-table>

        <Paginator
            v-on:update-pagination="updatePagination($event)"
            :num-pages="numPages"/>
      </v-col>
    </v-row>

    <v-dialog
        v-model="studentAddEditDialog"
        max-width="600">
      <StudentAddEdit
          :student-id="studentIdForEdit"
          v-on:student-add="studentAdd($event)"
          v-on:student-edit="studentEdit($event)"
          v-on:close-dialog="closeDialog"/>
    </v-dialog>

    <v-dialog
        v-model="studentDeleteDialog"
        max-width="400">
      <StudentDelete
          :student-id="studentIdForDelete"
          v-on:student-delete="studentDelete($event)"
          v-on:close-dialog="closeDialog"/>
    </v-dialog>
  </div>
</template>

<script>
import api from '/src/apis/api';
import sex from '/src/apis/enums';
import moment from 'moment';
import _ from 'lodash';
import StudentAddEdit from '/src/Components/Students/StudentAddEdit';
import StudentDelete from '/src/Components/Students/StudentDelete';
import Paginator from '/src/Components/Utils/Paginator';
import withPagination from '/src/Components/Utils/paginator.js';

export default {
  name: 'Students',

  components: { StudentAddEdit, StudentDelete, Paginator },

  data: () => ({
    headers: [
      { text: '№', value: 'id' },
      { text: 'Аватар', value: 'profilePhotoUrl' },
      { text: 'Фамилия', value: 'lastName' },
      { text: 'Имя', value: 'firstName' },
      { text: 'Отчество', value: 'middleName' },
      { text: 'Пол', value: 'sex' },
      { text: 'Дата рождения', value: 'birthday' },
      { text: 'Возраст', value: 'age' },
      { text: 'Готов вступать в секции', value: 'isReadyToJoinToSection' },
      { text: 'Является гражданином РФ', value: 'isCitizenOfRf' },
      { text: 'Секции', value: 'sections' },
      { text: 'Действия', value: 'actions', align: 'end' },
    ],
    tableData: [],
    pageSize: 10,
    page: 1,
    numPages: 1,

    filterForm: {},
    sex,

    studentAddEditDialog: false,
    studentDeleteDialog: false,

    studentIdForEdit: 0,
    studentIdForDelete: 0,
  }),

  computed: {
    emptyFilterForm: () => ({ firstName: '', lastName: '', sex: '' }),
  },

  methods: {
    addStudent() {
      this.studentAddEditDialog = true;
      this.studentIdForEdit = 0;
    },

    editStudent(studentId) {
      this.studentIdForEdit = studentId;
      this.studentAddEditDialog = true;
    },

    deleteStudent(studentId) {
      this.studentIdForDelete = studentId;
      this.studentDeleteDialog = true;
    },

    formatStudent: (student) => ({
      id: student.id,
      profilePhotoUrl: student.profilePhotoUrl,
      lastName: student.lastName,
      firstName: student.firstName,
      middleName: student.middleName || '-',
      sex: _.find(sex, (el) => el.type === student.sex).text,
      birthday: moment(student.birthday).format('DD.MM.YYYY'),
      age: student.age,
      isReadyToJoinToSection: student.isReadyToJoinToSection,
      isCitizenOfRf: student.isCitizenOfRf,
      sections: student.sections,
    }),

    getStudents() {
      withPagination(api.get('students/', {
        params: {
          expand: 'sections,sections.section',
          ...this.filterForm,
          pageSize: this.pageSize,
          page: this.page,
        },
      })).then((response) => {
        this.numPages = response.paginator.numPages;
        this.tableData = _.map(response.data, (item) => this.formatStudent(item));
      });
    },

    afterEditStudents() {
      this.studentAddEditDialog = false;
      this.studentDeleteDialog = false;
      this.studentIdForEdit = 0;
      this.studentIdForDelete = 0;
    },

    filter() {
      this.getStudents();
    },

    resetFilterForm() {
      this.$refs.filterForm.reset();
      this.getStudents();
    },

    updatePagination(data) {
      this.page = data.page;
      this.pageSize = data.pageSize;
      this.getStudents();
    },

    studentAdd(student) {
      this.tableData = _.concat(this.tableData, this.formatStudent(student));
      this.afterEditStudents();
    },

    studentEdit(student) {
      const studentIndex = _.findIndex(this.tableData, (el) => el.id === student.id);
      this.tableData.splice(studentIndex, 1, this.formatStudent(student));
      this.afterEditStudents();
    },

    studentDelete(studentId) {
      this.tableData = _.remove(this.tableData, (el) => el.id !== studentId);
      this.afterEditStudents();
    },

    closeDialog: () => this.afterEditStudents(),
  },

  created() {
    this.filterForm = this.emptyFilterForm;
    this.getStudents();
  },
};

</script>
