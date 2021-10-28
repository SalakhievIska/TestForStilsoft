<template>
  <v-card>
    <v-card-title class="text-h5 justify-center">
      {{ sectionId ? 'Изменить' : 'Добавление' }} секции
    </v-card-title>

    <v-form
        ref="form"
        v-model="valid"
        class="px-5">

      <v-row>
        <v-col cols="12">
          <v-text-field
              v-model="form.name"
              :rules="rules.name"
              label="Имя"
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

      <v-btn color="purple lighten-2" dark @click="saveSection">
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
import { requiredField, maxLengthField } from '/src/utils/validators';

export default {
  name: 'SectionAddEdit',

  props: ['sectionId'],

  data: () => ({
    valid: false,
    form: {},
    rules: {},
  }),

  computed: {
    emptyForm: () => ({ name: '' }),

    formRules: () => ({
      name: [
        (v) => requiredField(v),
        (v) => maxLengthField(v, 128, 'Название'),
      ],
    }),
  },

  methods: {
    closeDialog() {
      this.$emit('close-dialog');
    },

    saveSection() {
      if (this.$refs.form.validate()) {
        const section = { name: this.form.name };
        const params = { params: { expand: 'students,students.student' } };
        if (this.sectionId === 0) {
          api.post('sections/', section, params)
            .then((response) => this.$emit('section-add', response.data));
        } else {
          api.patch(`sections/${this.sectionId}/`, section, params)
            .then((response) => this.$emit('section-edit', response.data));
        }
      }
    },

    setFormData() {
      if (this.sectionId !== 0) {
        api.get(`sections/${this.sectionId}/`).then((response) => {
          this.form = { name: response.data.name };
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
    sectionId() {
      this.setFormData();
    },
  },

  mounted() {
    this.setFormData();
  },
};
</script>
