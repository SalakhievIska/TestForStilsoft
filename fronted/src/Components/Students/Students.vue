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

    <v-data-table
        :headers="headers"
        :items="tableData"
        class="px-10 my-5"
        locale="ru-RU">

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

    <v-dialog
        v-model="studentAddEditDialog"
        max-width="600">
      <StudentAddEdit :student-id="studentIdForEdit"/>
    </v-dialog>

    <v-dialog
        v-model="studentDeleteDialog"
        max-width="400">
      <StudentDelete :student-id="studentIdForDelete"/>
    </v-dialog>
  </div>
</template>

<script>
import api from '/src/apis/api';
import sex from '/src/apis/enums';
import bus from '/src/utils/bus';
import moment from 'moment';
import _ from 'lodash';
import StudentAddEdit from '/src/Components/Students/StudentAddEdit';
import StudentDelete from '/src/Components/Students/StudentDelete';

export default {
  name: 'Students',

  components: { StudentAddEdit, StudentDelete },

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

    studentAddEditDialog: false,
    studentDeleteDialog: false,

    studentIdForEdit: 0,
    studentIdForDelete: 0,
  }),

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
      api.get('students/', {
        params: { expand: 'sections,sections.section' },
      }).then((response) => {
        this.tableData = _.map(response.data, (item) => this.formatStudent(item));
      }).catch((error) => console.log(error));
    },

    afterEditStudents() {
      this.studentAddEditDialog = false;
      this.studentDeleteDialog = false;
      this.studentIdForEdit = 0;
      this.studentIdForDelete = 0;
    },
  },

  created() {
    this.getStudents();

    bus.$on('student-add', (newStudent) => {
      this.tableData = _.concat(this.tableData, this.formatStudent(newStudent));
      this.afterEditStudents();
    });

    bus.$on('student-edit', (student) => {
      const studentIndex = _.findIndex(this.tableData, (el) => el.id === student.id);
      this.tableData.splice(studentIndex, 1, this.formatStudent(student));
      this.afterEditStudents();
    });

    bus.$on('student-delete', (studentId) => {
      this.tableData = _.remove(this.tableData, (el) => el.id !== studentId);
      this.afterEditStudents();
    });

    bus.$on('close-dialog', () => this.afterEditStudents());
  },
};

</script>
