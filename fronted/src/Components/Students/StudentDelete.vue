<template>
  <v-card>
    <v-card-title class="text-h5 justify-center">
      Удаление студента №{{ studentId }}
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
import bus from '/src/utils/bus';

export default {
  name: 'StudentDelete',

  props: ['studentId'],

  methods: {
    submitDelete() {
      api.delete(`students/${this.studentId}/`)
        .then(() => bus.$emit('student-delete', this.studentId));
    },

    closeDialog: () => bus.$emit('close-dialog'),
  },
};
</script>
