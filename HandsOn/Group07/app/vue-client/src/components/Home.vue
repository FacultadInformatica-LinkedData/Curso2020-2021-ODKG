<template>
  <v-layout wrap>
    <v-flex mb-4>
      <v-row justify="center" class="mx-2">
        <h1 class="display-2 font-weight-bold">
          PROJECTS UNDER HORIZON 2020
        </h1>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search by title"
            single-line
            hide-details
            class="shrink mb-n10"
          ></v-text-field>
        </v-row>
      <v-row no-gutters justify="center" class="mx-n16">
          <v-col
            v-for="(project,key,index) in res"
            :key="project.label"
            cols="3"
          >
            <v-card v-if="res" class=" ma-1" outlined tile>
              <v-responsive :aspect-ratio="8 / 12">
                <v-card-title v-if="titles"
                  >{{titles[index].o.value}} ({{acronyms[index].o.value}})</v-card-title
                >

                <v-card-text justify="left">
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Objective:</span> {{objectives[index].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Programme:</span> {{programmes[index].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Topic:</span> {{topics[index].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Total cost:</span> {{costs[index].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Maximum contribution:</span> {{contributions[index].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Dates:</span> {{ends[index].o.value.slice(0,10)}} - {{starts[index].o.value.slice(0,10)}}</div>
                </v-card-text>

                <v-card-actions justify="center" class="card-actions">
                  <v-btn text @click="visitWebpage(urls[index].o.value.replace('~IRI',''))">VISIT WEBPAGE</v-btn>
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
    res:""
  }),
  async created() {
    this.res = await CommonRepository.getProjects();
  },
  methods: {
    async visitWebpage(externalURL) {
      window.open(externalURL);
    }
  },
  computed: {
    filteredList() {
      return this.projects.filter(project => {
          return project.title.toLowerCase().includes(this.search.toLowerCase());      
      });
    },
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
  left: 23%;
}
</style>
