<template>
  <v-layout wrap>
    <v-flex mb-4>
      <h1 class="display-2 font-weight-bold">
        RESEARCHERS UNDER HORIZON 2020
      </h1>
      <v-row class="mb-2">
        <v-col cols="8">
          <v-toolbar dense>
            <v-text-field
              hide-details
              label="Search by name"
              single-line
              v-model="searchName"
            ></v-text-field>
            <v-btn icon @click="searchByName(searchName)"
              ><v-icon>mdi-magnify</v-icon></v-btn
            >
            <v-text-field
              hide-details
              label="Search by organization"
              single-line
              v-model="searchOrg"
            ></v-text-field>
            <v-btn icon @click="searchByOrganization(searchOrg)"
              ><v-icon>mdi-magnify</v-icon></v-btn
            >
          </v-toolbar>
        </v-col>
      </v-row>
      <v-row no-gutters justify="center" class="mx-n16">
        <v-col
          v-for="(researcher, key) in researchers"
          :key="researcher.id"
          :v-bind="i + 1"
          cols="3"
        >
          <v-card v-if="res" class=" ma-1" outlined tile>
            <v-responsive :aspect-ratio="4 / 2">
              <v-card-title v-if="titles" justify="center"
                >{{ titles[key].o.value }}.
                {{ names[key].o.value }}</v-card-title
              >
              <v-card-actions justify="center" class="card-actions">
                <v-btn text @click="visitWebpage(urls[key].o.value)"
                  >VISIT WEBPAGE</v-btn
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
    searchName: "",
    searchOrg: "",
    i: 0,
    res: "",
    researchers: []
  }),
  async created() {
    this.res = await CommonRepository.getResearchers();
    this.researchers = this.res.data.results.bindings.filter(resAux => {
      return resAux.p.value == "http://www.w3.org/2000/01/rdf-schema#label";
    });
  },
  methods: {
    titleTemplate(chunk) {
      const truncatedChunk =
        chunk.length > 65 ? `${chunk.substr(0, 65 - 3)}...` : chunk;
      return truncatedChunk;
    },
    async visitWebpage(externalURL) {
      window.open(externalURL);
    },
    async searchByOrganization(searchOrg) {
      this.res = "";
      this.res = await CommonRepository.getResearchersOrganization(searchOrg);
      this.researchers = [];
      this.researchers = this.res.data.results.bindings.filter(resAux => {
        return resAux.p.value == "http://www.w3.org/2000/01/rdf-schema#label";
      });
    },
    async searchByName(name) {
      this.res = "";
      this.res = await CommonRepository.getResearchersByName(name);
      this.researchers = [];
      this.researchers = this.res.data.results.bindings.filter(resAux => {
        return resAux.p.value == "http://www.w3.org/2000/01/rdf-schema#label";
      });
    }
  },
  computed: {
    filteredList() {
      return this.res.data.results.bindings
        .filter(researcher => {
          return (
            researcher.p.value ==
              "http://www.w3.org/2000/01/rdf-schema#label" ||
            researcher.p.value == "http://xmlns.com/foaf/0.1/title" ||
            researcher.p.value == "http://www.w3.org/2002/07/owl#sameAs"
          );
        })
        .filter(name => {
          return name.o.value.toLowerCase().includes(this.search.toLowerCase());
        });
    },
    titles() {
      return this.res.data.results.bindings.filter(researcher => {
        return researcher.p.value == "http://xmlns.com/foaf/0.1/title";
      });
    },
    names() {
      return this.res.data.results.bindings.filter(researcher => {
        return (
          researcher.p.value == "http://www.w3.org/2000/01/rdf-schema#label"
        );
      });
    },
    urls() {
      return this.res.data.results.bindings.filter(researcher => {
        return researcher.p.value == "http://www.w3.org/2002/07/owl#sameAs";
      });
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
