import http from "./httpService";
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl + "/movies";

export function getSupportedTasks() {
  const url = `${apiEndpoint}/supportedtasks`;
  return http.get(url);
}

export function getTaskQueue() {
  const url = `${apiEndpoint}/taskqueue`;
  return http.get(url);
}

export function putTask(task) {
  const url = `${apiEndpoint}/put`;
  return http.post(url, task);
}

export function insertTask(index, task) {
  const url = `${apiEndpoint}/insert/${index}`;
  return http.post(url, task);
}

export function removeTask(task) {
  const url = `${apiEndpoint}/remove/${task.id}`;
  return http.post(url);
}

export default {
  getSupportedTasks,
  getTaskQueue,
  putTask,
  insertTask,
  removeTask
};
