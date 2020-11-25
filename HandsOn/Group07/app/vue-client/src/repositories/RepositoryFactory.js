import CommonRepository from "./CommonRepository";

const repositories = {
  common: CommonRepository
};

export default {
  get: name => repositories[name]
};
