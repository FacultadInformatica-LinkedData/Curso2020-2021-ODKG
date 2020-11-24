import HTTP from "@/common/http";

export default {
  async showAll() {
    const response = await HTTP.get(`all`);
    return response;
  },
  async getResearchers() {
    const response = await HTTP.get(`researchers`);
    return response;
  },
  async getOrganizations() {
    const response = await HTTP.get(`organizations`);
    return response;
  },
  async getProjects() {
    const response = await HTTP.get(`projects`);
    return response;
  },
  async getParticipations() {
    const response = await HTTP.get(`participations`);
    return response;
  },
  async getOrganizationsByCountry(country) {
    const response = await HTTP.get(`organizations/${country}`);
    return response;
  },
  async getOrganizationsByName(name) {
    const response = await HTTP.get(`organizations/name/${name}`);
    return response;
  },
  async getResearchersByName(name) {
    const response = await HTTP.get(`researchers/name/${name}`);
    return response;
  },
  async getProjectsByTitle(title) {
    const response = await HTTP.get(`projects/title/${title}`);
    return response;
  },
  async getProjectContribution(Contribution) {
    const response = await HTTP.get(`projects/${Contribution}`);
    return response;
  },
  async getResearchersOrganization(organization) {
    const response = await HTTP.get(`researchers/${organization}`);
    return response;
  }
};
