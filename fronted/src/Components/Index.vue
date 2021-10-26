<template>
  <v-card>
    <v-tabs
        v-model="tab"
        background-color="purple darken-2"
        centered
        dark
        icons-and-text
        class="rounded-0">
      <v-tabs-slider color="light-blue"></v-tabs-slider>

      <v-tab v-for="item in items" :key="item.tab">
        {{ item.title }}
        <v-icon>{{ item.icon }}</v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-card flat>
          <Students/>
        </v-card>
      </v-tab-item>

      <v-tab-item>
        <v-card flat>
          <Sections/>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
import Students from './Students/Students';
import Sections from './Sections/Sections';

export default {
  name: 'Index',

  components: {
    Sections, Students,
  },

  data: () => ({
    tab: null,
    items: [
      {
        tab: 'students',
        title: 'Студенты',
        icon: 'fas fa-user-graduate',
      },
      {
        tab: 'sections',
        title: 'Секции',
        icon: 'fas fa-graduation-cap',
      },
    ],
  }),
};

</script>
