<template>
  <v-layout wrap>
    <v-flex mb-4>
        <h1 class="display-2 font-weight-bold">
          PROJECTS UNDER HORIZON 2020
        </h1>
        <v-row class="mb-2">
          <v-col cols=9>
          <v-toolbar dense>
            <v-text-field
              hide-details
              label="Search by name"
              v-model="searchName"
            ></v-text-field>
            <v-btn icon @click="searchByName(searchName)"><v-icon>mdi-magnify</v-icon></v-btn>
            <v-text-field
              hide-details
              persistent-hint
              label="Search projects with contribution greater than:"
              v-model="searchContribution"
            ></v-text-field>
            <v-btn icon @click="searchByContribution(searchContribution)"><v-icon>mdi-magnify</v-icon></v-btn>
          </v-toolbar>
          </v-col>
        </v-row>
      <v-row no-gutters justify="center" class="mx-n16">
          <v-col
            v-for="(project,key) in projects"
            :key="project.id"
            cols="4"
          >
            <v-card v-if="res" class="ma-1 pa-n1" outlined tile>
              <v-responsive :aspect-ratio="7 / 9">
                <v-card-title v-if="titles"
                  >{{titles[key].o.value}} ({{acronyms[key].o.value}})</v-card-title
                >

                <v-card-text justify="left">
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Objective:</span> {{objectives[key].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Programme:</span> {{programmes[key].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Topic:</span> {{topics[key].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Total cost:</span> {{costs[key].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Maximum contribution:</span> {{contributions[key].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Dates:</span> {{ends[key].o.value.slice(0,10)}} - {{starts[key].o.value.slice(0,10)}}</div>
                </v-card-text>

                <v-card-actions justify="center" class="card-actions">
                  <v-btn text @click="visitWebpage(urls[key].o.value.replace('~IRI',''))">VISIT WEBPAGE</v-btn>
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
    searchContribution: "",
    searchTitle: "",
    res:"",
    projects: []
  }),
  async created() {
    this.res = await CommonRepository.getProjects();
    this.projects = this.res.data.results.bindings.filter(resAux => {
      return (resAux.p.value == "http://www.w3.org/2000/01/rdf-schema#label");
    })
  },
  methods: {
    async visitWebpage(externalURL) {
      window.open(externalURL);
    },
    async searchByContribution(contribution){
      this.res = "";
      this.res = await CommonRepository.getProjectContribution(contribution);
      this.projects=[];
      this.projects = this.res.data.results.bindings.filter(resAux => {
          return (resAux.p.value == "http://www.w3.org/2000/01/rdf-schema#label");
        })
    },
    async searchByName(name){
      this.res = "";
      this.res = await CommonRepository.getProjectsByTitle(name);
      this.projects=[];
      this.projects = this.res.data.results.bindings.filter(resAux => {
          return (resAux.p.value == "http://www.w3.org/2000/01/rdf-schema#label");
        })
    }
  },
  computed: {
    titles(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://purl.org/dc/terms/title");
      })
    },
    topics(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://purl.org/dc/terms/subject");
      })
    },
    contributions(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://www.example.org/group07/ontology/contribution");
      })
    },
    urls(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://www.w3.org/2006/vcard/ns#url");
      })
    },
    objectives(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "https://w3id.org/dingo#objective");
      })
    },
    costs(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://dbpedia.org/ontology/cost");
      })
    },
    ends(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://schema.org/endDate");
      })
    },
    starts(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://schema.org/startDate");
      })
    },
    acronyms(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://www.eurocris.org/ontologies/cerif/1.3#acronym");
      })
    },
    programmes(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://www.example.org/group07/ontology/programme");
      })
    },
    records(){
      return this.res.data.results.bindings.filter(proj => {
        return (proj.p.value == "http://www.w3.org/ns/dcat#record");
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
  bottom: 0;
  left: 30%;
}
</style>
