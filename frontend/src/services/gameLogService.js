import http from "./httpService";
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl;

export function getScreenShot() {
  const url = `${apiEndpoint}/screenshot`;
  return http.get(url);
}

export default {
  getScreenShot
};
