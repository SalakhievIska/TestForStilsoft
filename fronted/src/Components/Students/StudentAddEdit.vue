<template>
  <v-card>
    <v-card-title class="text-h5 justify-center">
      {{ studentId ? 'Изменить' : 'Добавление' }} студента
    </v-card-title>

    <v-form
        ref="form"
        v-model="valid"
        class="px-5">

      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
              v-model="form.firstName"
              :rules="rules.firstName"
              label="Имя"
              required>
          </v-text-field>
        </v-col>

        <v-col cols="12" md="6">
          <v-text-field
              v-model="form.lastName"
              :rules="rules.lastName"
              label="Фамилия"
              required>
          </v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
              v-model="form.middleName"
              :rules="rules.middleName"
              label="Отчество"
              required>
          </v-text-field>
        </v-col>

        <v-col cols="12" md="6">
          <v-menu
              v-model="birthdayMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y>
            <template v-slot:activator="{ on }">
              <v-text-field
                  label="День рождения"
                  readonly
                  :value="form.birthday"
                  :rules="rules.birthday"
                  v-on="on">
              </v-text-field>
            </template>
            <v-date-picker
                locale="ru-ru"
                v-model="birthdayVal"
                no-title
                @input="onBirthdayInput">
            </v-date-picker>
          </v-menu>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12">
          <v-radio-group
              v-model="form.sex"
              :rules="rules.sex"
              row>
            <v-radio
                v-for="item in sex"
                :key="item.type"
                :label="item.text"
                :value="item.type">
            </v-radio>
          </v-radio-group>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" md="6">
          <v-checkbox
              v-model="form.isReadyToJoinToSection"
              label="Готов вступать в секции">
          </v-checkbox>
        </v-col>

        <v-col cols="12" md="6">
          <v-checkbox
              v-model="form.isCitizenOfRf"
              label="Является гражданином РФ">
          </v-checkbox>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12">
          <v-text-field
              v-model="form.profilePhotoUrl"
              :rules="rules.profilePhotoUrl"
              label="Ссылка на фотографию профиля"
              required>
          </v-text-field>
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

      <v-btn color="purple lighten-2" dark @click="saveStudent">
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
import sex from '/src/apis/enums';
import { requiredField, maxLengthField, urlField } from '/src/utils/validators';
import moment from 'moment';

export default {
  name: 'StudentAddEdit',

  props: ['studentId'],

  data: () => ({
    birthdayVal: null,
    birthdayMenu: false,
    valid: false,
    form: {},
    rules: {},
    sex,
    currentDateFormat: 'DD.MM.YYYY',
  }),

  computed: {
    emptyForm: () => ({
      firstName: '',
      lastName: '',
      middleName: '',
      birthday: '',
      sex: '',
      isReadyToJoinToSection: true,
      isCitizenOfRf: true,
      profilePhotoUrl: '',
    }),

    formRules: () => ({
      firstName: [
        (v) => requiredField(v),
        (v) => maxLengthField(v, 128, 'Имя'),
      ],
      lastName: [
        (v) => requiredField(v),
        (v) => maxLengthField(v, 128, 'Фамилия'),
      ],
      middleName: [
        (v) => maxLengthField(v, 128, 'Отчество'),
      ],
      birthday: [
        (v) => requiredField(v),
      ],
      sex: [
        (v) => requiredField(v),
      ],
      profilePhotoUrl: [
        (v) => maxLengthField(v, 128, 'Ссылка на фотографию профиля'),
        (v) => urlField(v),
      ],
    }),
  },

  methods: {
    closeDialog: () => this.$emit('close-dialog'),

    saveStudent() {
      if (this.$refs.form.validate()) {
        const student = {
          lastName: this.form.lastName,
          firstName: this.form.firstName,
          middleName: this.form.middleName || '',
          sex: this.form.sex,
          birthday: moment(this.form.birthday, this.currentDateFormat).format('YYYY-MM-DD'),
          isReadyToJoinToSection: this.form.isReadyToJoinToSection,
          isCitizenOfRf: this.form.isCitizenOfRf,
          profilePhotoUrl: this.form.profilePhotoUrl || '',
        };
        if (this.studentId === 0) {
          api.post('students/', student)
            .then((response) => this.$emit('student-add', response.data));
        } else {
          api.patch(`students/${this.studentId}/`, student)
            .then((response) => this.$emit('student-edit', response.data));
        }
      }
    },

    onBirthdayInput(val) {
      this.form.birthday = moment(val).format(this.currentDateFormat);
      this.birthdayMenu = false;
    },

    setFormData() {
      if (this.studentId !== 0) {
        api.get(`students/${this.studentId}/`).then((response) => {
          this.form = {
            firstName: response.data.firstName,
            lastName: response.data.lastName,
            middleName: response.data.middleName || '',
            birthday: moment(response.data.birthday).format(this.currentDateFormat),
            sex: response.data.sex,
            isReadyToJoinToSection: response.data.isReadyToJoinToSection,
            isCitizenOfRf: response.data.isCitizenOfRf,
            profilePhotoUrl: response.data.profilePhotoUrl,
          };
          this.birthdayVal = response.data.birthday;
        });
      } else {
        this.$refs.form.resetValidation();
        this.form = this.emptyForm;
      }
    },
  },

  created() {
    this.rules = this.formRules;
    this.form = this.emptyForm;
  },

  watch: {
    studentId() {
      this.setFormData();
    },
  },

  mounted() {
    this.setFormData();
  },
};
</script>
