<template>
  <v-card>
    <v-card-title class="text-h5 justify-center">
      Отчисление студента из секции
    </v-card-title>

    <v-card-actions class="justify-center mt-4">
      <v-btn color="grey lighten-2" @click="closeDialog">
        <v-icon small class="mx-1">
          fas fa-times
        </v-icon>
        Отменить
      </v-btn>

      <v-btn color="purple lighten-2" dark @click="submitDelete">
        <v-icon small class="mx-1">
          fas fa-check
        </v-icon>
        Удалить
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api from '/src/apis/api';

export default {
  name: 'StudentInSectionDelete',

  props: ['studentInSectionId'],

  data: () => ({
    sectionId: 0,
  }),

  methods: {
    closeDialog: () => this.$emit('close-dialog'),

    submitDelete() {
      api.get(`students-in-sections/${this.studentInSectionId}/`).then((response) => {
        this.sectionId = response.data.section;
        api.delete(`students-in-sections/${this.studentInSectionId}/`)
          .then(() => {
            api.get(`sections/${this.sectionId}/`, {
              params: { expand: 'students,students.student' },
            }).then((rResponse) => this.$emit('section-edit', rResponse.data));
          });
      });
    },
  },
};
</script>
