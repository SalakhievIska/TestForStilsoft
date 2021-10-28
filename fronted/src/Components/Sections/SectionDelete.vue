<template>
  <v-card>
    <v-card-title class="text-h5 justify-center">
      Удаление секции №{{ sectionId }}
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
  name: 'SectionDelete',

  props: ['sectionId'],

  methods: {
    closeDialog() {
      this.$emit('close-dialog');
    },

    submitDelete() {
      api.delete(`sections/${this.sectionId}/`)
        .then(() => this.$emit('section-delete', this.sectionId));
    },
  },
};
</script>
