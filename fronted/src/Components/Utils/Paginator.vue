<template>
  <v-row class="mb-5 px-10">
    <v-col cols="3">
      <v-select
          :items="[1, 5, 10, 20]"
          v-model="pageSize"
          prefix="Показывать по:"
          outlined
          dense
          item-color="purple lighten-2">
      </v-select>
    </v-col>

    <v-col cols="9" class="d-flex justify-end">
      <v-pagination
          v-model="page"
          circle
          :length="numPages"
          :total-visible="5"
          color="purple lighten-2"
          next-icon="fas fa-angle-right"
          prev-icon="fas fa-angle-left">
      </v-pagination>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Paginator',
  props: ['numPages'],

  data: () => ({
    pageSize: 10,
    page: 1,
  }),

  watch: {
    pageSize() {
      this.page = 1;
      this.$emit('update-pagination', { page: this.page, pageSize: this.pageSize });
    },
    page() {
      this.$emit('update-pagination', { page: this.page, pageSize: this.pageSize });
    },
  },
};
</script>
