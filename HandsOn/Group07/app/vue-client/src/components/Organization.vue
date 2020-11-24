<template>
  <v-layout wrap>
    <v-flex mb-4>
      <h1 class="display-2 font-weight-bold">
        ORGANIZATIONS UNDER HORIZON 2020
      </h1>
      <v-row class="mb-2">
          <v-col cols=8>
          <v-toolbar dense>
            <v-text-field
              hide-details
              label="Search by name"
              single-line
              v-model="searchName"
            ></v-text-field>
            <v-btn icon @click="searchByName(searchName)"><v-icon>mdi-magnify</v-icon></v-btn>
            <v-text-field
              hide-details
              label="Search by country"
              single-line
              v-model="searchCountry"
            ></v-text-field>
            <v-btn icon @click="searchByCountry(searchCountry)"><v-icon>mdi-magnify</v-icon></v-btn>
          </v-toolbar>
          </v-col>
        </v-row>
      <v-row no-gutters justify="center" class="mx-n16">
          <v-col
            v-for="(org,key) in organizations"
            :key="org.id"
            cols="3"
          >
            <v-card v-if="orgs" class=" ma-1" outlined tile>
              <div>
              <v-responsive :aspect-ratio="8 / 10">
                <v-card-title v-if="names"
                  >{{ names[key].o.value }} ({{abbreviations[key].o.value}})</v-card-title
                >
                <v-card-text justify="left">
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Country:</span> {{countries[key].o.value.slice(48).replaceAll("%20"," ")}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >City:</span> {{localities[key].o.value.slice(45).replaceAll("%20"," ")}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Street:</span> {{streets[key].o.value.slice(47).replaceAll("%20"," ")}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Postal code:</span> {{postals[key].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Activity type:</span> {{types[key].o.value}}</div>
                  </v-card-text>
                <v-card-actions justify="center" class="card-actions">
                  <v-btn text @click="visitWebpage(urls[key].o.value)">VISIT WEBPAGE</v-btn
      >
                </v-card-actions>
              </v-responsive></div>
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
    searchCountry: "",
    searchName: "",
    orgs: "",
    organizations:[]
  }),
  async created() {
    this.orgs = await CommonRepository.getOrganizations();
    this.organizations = this.orgs.data.results.bindings.filter(org => {
          return (org.p.value == "http://www.w3.org/2000/01/rdf-schema#label");
        })
  },
  methods: {
    async visitWebpage(externalURL) {
      window.open(externalURL);
    },
    async searchByName(name){
      this.orgs = "";
      this.orgs = await CommonRepository.getOrganizationsByName(name);
      this.organizations=[];
      this.organizations = this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://www.w3.org/2000/01/rdf-schema#label");
      });
    },
    async searchByCountry(country){
      this.orgs = "";
      this.orgs = await CommonRepository.getOrganizationsByCountry(country);
      this.organizations=[];
      this.organizations = this.orgs.data.results.bindings.filter(org => {
          return (org.p.value == "http://www.w3.org/2000/01/rdf-schema#label");
        })
    }
  },
  computed: {
    names(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://www.w3.org/2006/vcard/ns#organization-name");
      })
    },
    abbreviations(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://dbpedia.org/ontology/abbreviation");
      })
    },
    localities(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://www.w3.org/2006/vcard/ns#hasLocality");
      })
    },
    postals(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://www.w3.org/2006/vcard/ns#postal-code");
      })
    },
    types(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://dbpedia.org/ontology/type");
      })
    },
    urls(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://www.w3.org/2002/07/owl#sameAs");
      })
    },
    streets(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://www.w3.org/2006/vcard/ns#hasStreetAddress");
      })
    },
    countries(){
      return this.orgs.data.results.bindings.filter(org => {
        return (org.p.value == "http://schema.org/addressCountry");
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
