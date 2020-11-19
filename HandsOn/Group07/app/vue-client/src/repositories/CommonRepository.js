import HTTP from "@/common/http";

export default {
  async showAll() {
    const response = await HTTP.get("all");
    return response;
  },
  async getResearchers() {
    const response = await HTTP.get("researchers");
    return response;
  },
  async getOrganizations() {
    const response = await HTTP.get("organizations");
    return response;
  },
  async getProjects() {
    const response = await HTTP.get("projects");
    return response;
  },
  async getParticipations() {
    const response = await HTTP.get("participations");
    return response;
  }
};
