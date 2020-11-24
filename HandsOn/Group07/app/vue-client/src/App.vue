<template>
  <v-app>
    <!-- Notificaciones usando vue-notification -->
    <notifications :max="3" :width="400" position="top center" />

    <!-- Barra horizontal superior -->
    <div>
      <v-app-bar app color="primary" dark>

        <v-toolbar-title
          ><router-link style="color:white" :to="{ name: 'Home' }"
            >PROJEU: LINKED RESEARCH AND INNOVATION PROJECTS</router-link
          ></v-toolbar-title
        >

        <v-spacer></v-spacer>

        <template v-slot:extension>
          <v-tabs align-with-title>
            <v-tab to="/">HOME</v-tab>
            <v-tab to="/organizations">ORGANIZATIONS</v-tab>
            <v-tab to="/researchers">RESEARCHERS</v-tab>
          </v-tabs>
        </template>
      </v-app-bar>
    </div>

    <v-main>
      <v-container fluid>
        <!-- Contenido gestionado por vue-router -->
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import store from "./common/store";

export default {
  data: () => ({
    app: store.state.app,
    items: [
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me 2" }
    ]
  }),
  computed: {
  },
  methods: {
  }
};
</script>

<style lang="scss" src="./App.scss"></style>
