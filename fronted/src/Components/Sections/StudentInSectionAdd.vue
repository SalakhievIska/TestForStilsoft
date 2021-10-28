<template>
  <v-card>
    <v-card-title class="text-h5 justify-center">
      Зачисление студента в секцию {{ section.name }}
    </v-card-title>

    <v-form
        ref="form"
        v-model="valid"
        class="px-5">

      <v-row>
        <v-col cols="12">
          <div v-for="error in nonFieldErrors" :key="error" class="red--text">
            {{ error }}
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12">
          <v-select
              v-model="form.student"
              :items="students"
              :item-text="getItemText"
              item-value="id"
              label="Студент"
              persistent-hint
              return-object
              single-line
              :rules="rules.student"
              no-data-text="Нет доступных студентов">
          </v-select>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12">
          <v-menu
              v-model="joinDateMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y>
            <template v-slot:activator="{ on }">
              <v-text-field
                  label="Дата зачисления"
                  readonly
                  :value="form.joinDate"
                  :rules="rules.joinDate"
                  v-on="on">
              </v-text-field>
            </template>
            <v-date-picker
                locale="ru-ru"
                v-model="joinDateVal"
                no-title
                @input="onJoinDateInput">
            </v-date-picker>
          </v-menu>
        </v-col>
      </v-row>

    </v-form>

    <v-card-actions class="justify-center mt-4">
      <v-btn color="grey lighten-2" @click="closeDialog">
        <v-icon small class="mx-1">
          fas fa-times
        </v-icon>
        Отменить
      </v-btn>

      <v-btn color="purple lighten-2" dark @click="saveStudentInSection">
        <v-icon small class="mx-1">
          fas fa-check
        </v-icon>
        Сохранить
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api from '/src/apis/api';
import { requiredField } from '/src/utils/validators';
import _ from 'lodash';
import moment from 'moment';

export default {
  name: 'StudentInSectionAdd',

  props: ['sectionId'],

  data: () => ({
    valid: false,
    form: {},
    rules: {},
    joinDateVal: null,
    joinDateMenu: false,
    currentDateFormat: 'DD.MM.YYYY',
    students: [],
    section: {},
    nonFieldErrors: [],
  }),

  computed: {
    emptyForm: () => ({ student: '', joinDate: '' }),

    formRules: () => ({
      student: [(v) => requiredField(v)],
      joinDate: [(v) => requiredField(v)],
    }),
  },

  methods: {
    getItemText: (val) => `${val.lastName} ${val.firstName}`,

    closeDialog() {
      this.$emit('close-dialog');
    },

    saveStudentInSection() {
      if (this.$refs.form.validate()) {
        const studentInSection = {
          section: this.section.id,
          student: this.form.student.id,
          joinDate: moment(this.form.joinDate, this.currentDateFormat).format('YYYY-MM-DD'),
        };
        api.post('students-in-sections/', studentInSection)
          .then((response) => {
            api.get(`sections/${response.data.section}/`, {
              params: { expand: 'students,students.student' },
            }).then((rResponse) => this.$emit('section-edit', rResponse.data));
          }).catch((error) => {
            const errorData = error.response.data;
            if (errorData) {
              if (errorData.nonFieldErrors) this.nonFieldErrors = errorData.nonFieldErrors;
            }
          });
      }
    },

    onJoinDateInput(val) {
      this.form.joinDate = moment(val).format(this.currentDateFormat);
      this.joinDateMenu = false;
    },

    setFormData() {
      this.nonFieldErrors = [];
      if (this.sectionId !== 0) {
        api.get(`sections/${this.sectionId}/`, {
          params: { expand: 'students,students.student' },
        }).then((response) => {
          this.section = response.data;
          api.get('students/').then((rResponse) => {
            const studentsIds = _.map(response.data.students, (item) => item.student.id);
            this.students = _.filter(rResponse.data,
              (item) => !_.includes(studentsIds, item.id) && item.isReadyToJoinToSection);
          });
        });
      } else {
        this.$refs.form.resetValidation();
        this.$refs.form.reset();
      }
    },
  },

  created() {
    this.rules = this.formRules;
    this.form = this.emptyForm;
  },

  watch: {
    sectionId() {
      this.setFormData();
    },
  },

  mounted() {
    this.setFormData();
  },
};
</script>
