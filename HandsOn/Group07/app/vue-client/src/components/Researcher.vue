<template>
  <v-layout wrap>
    <v-flex mb-4>
      <v-row justify="center" class="mx-2">
        <h1 class="display-2 font-weight-bold">
          RESEARCHERS
        </h1>
      
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search by name"
            single-line
            hide-details
            class="shrink mb-n10"
          ></v-text-field>
        </v-row>
      <v-row no-gutters justify="center" class="mx-n16">
          <v-col
            v-for="(researcher, key, index) in res"
            :key="researcher.id"
            :v-bind="i+1"
            cols="3"
          >
            <v-card v-if="res" class=" ma-1" outlined tile>
              <v-responsive :aspect-ratio="4 / 2">
                <v-card-title v-if="titles" justify="center"
                  >{{titles[index].o.value}}. {{names[index].o.value}}</v-card-title
                >
                <v-card-actions justify="center" class="card-actions">
                  <v-btn text @click="visitWebpage(urls[index].o.value)">VISIT WEBPAGE</v-btn
      >
                </v-card-actions>
              </v-responsive>
            </v-card>
          </v-col>
        </v-row>
    </v-flex>
  </v-layout>
</template>

<script>
import RepositoryFactory from "@/repositories/RepositoryFactory";
const CommonRepository = RepositoryFactory.get("common");

export default {
  data: () => ({
    search: "",
    i:0,
    res:""
  }),
  async created() {
    this.res = await CommonRepository.getResearchers();
  },
  methods: {
    titleTemplate(chunk) {
      const truncatedChunk =
        chunk.length > 65 ? `${chunk.substr(0, 65 - 3)}...` : chunk;
      return truncatedChunk;
    },
    async visitWebpage(externalURL) {
      window.open(externalURL);
    }
  },
  computed: {
    filteredList() {
      return this.res.data.results.bindings.filter(researcher => {
        return ((researcher.p.value == "http://www.w3.org/2000/01/rdf-schema#label") || (researcher.p.value == "http://xmlns.com/foaf/0.1/title") || (researcher.p.value == "http://www.w3.org/2002/07/owl#sameAs") );
      }).filter(name => {
          return name.o.value.toLowerCase().includes(this.search.toLowerCase());      
      });
    },
    titles(){
      return this.res.data.results.bindings.filter(researcher => {
        return (researcher.p.value == "http://xmlns.com/foaf/0.1/title");
      })
    },
    names(){
      return this.res.data.results.bindings.filter(researcher => {
        return (researcher.p.value == "http://www.w3.org/2000/01/rdf-schema#label");
      })
    },
    urls(){
      return this.res.data.results.bindings.filter(researcher => {
        return (researcher.p.value == "http://www.w3.org/2002/07/owl#sameAs");
      })
    }
  }
};
</script>

<style scoped>
h1 {
  margin-top: 30px;
  margin-bottom: 30px;
}
.card-actions {
  position: absolute;
  left: 23%;
}
</style>
