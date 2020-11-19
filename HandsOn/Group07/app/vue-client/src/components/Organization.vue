<template>
  <v-layout wrap>
    <v-flex mb-4><v-row justify="center" class="mb-2">
      <h1 class="display-2 font-weight-bold">
        ORGANIZATIONS
      </h1>
      
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
            class="shrink mb-n10"
          ></v-text-field>
        </v-row>
      <v-row no-gutters justify="center" class="mx-n16">
          <v-col
            v-for="(org,key,index) in orgs"
            :key="org.label"
            cols="3"
          >
            <v-card v-if="orgs" class=" ma-1" outlined tile>
              <v-responsive :aspect-ratio="8 / 10">
                <v-card-title v-if="names"
                  >{{ names[index].o.value }} ({{abbreviations[index].o.value}})</v-card-title
                >

                <v-card-text justify="left">
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Country:</span> {{countries[index].o.value.slice(48).replaceAll("%20"," ")}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >City:</span> {{localities[index].o.value.slice(45).replaceAll("%20"," ")}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Street:</span> {{streets[index].o.value.slice(47).replaceAll("%20"," ")}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Postal code:</span> {{postals[index].o.value}}</div>
                  <div><span style="font-weight:bold; font-size:1.1em;"
                                  >Activity type:</span> {{types[index].o.value}}</div>
                  </v-card-text>
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
    orgs:""
  }),
  async created() {
    this.orgs = await CommonRepository.getOrganizations();
  },
  methods: {
    async visitWebpage(externalURL) {
      window.open(externalURL);
    }
  },
  computed: {
    filteredList() {
      return this.organizations.filter(org => {
          return org.name.toLowerCase().includes(this.search.toLowerCase());      
      });
    },
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
