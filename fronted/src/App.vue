<template>
  <v-app>
    <v-app-bar
        app
        color="purple darken-4"
        dark>
      <v-spacer></v-spacer>

      <div class="d-flex align-center">
        <v-icon large>fas fa-university</v-icon>
        <div class="text-h4 font-weight-medium ml-2">Study</div>
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <Index/>
    </v-main>
  </v-app>
</template>

<script>
import Index from './Components/Index';

export default {
  name: 'App',
  components: { Index },
  metaInfo: {
    title: 'Study',
    titleTemplate: '%s | Test Project',
  },
};
</script>
