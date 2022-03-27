import axios from "axios";
import * as querystring from "querystring";


export const axiosClient = axios.create({
    baseURL: 'http://192.168.1.219:8000/',
    timeout: 6000,
    paramsSerializer: params => {
        return querystring.stringify(params)
    }
});

axiosClient.interceptors.request.use(function (config) {
    return config;
    }, function (error){
    return Promise.reject(error);
})

axiosClient.interceptors.response.use(function (response) {
    return response;
    }, function (error){
    return Promise.reject(error);
})


const { get, post, put, delete: destroy } = axiosClient;
export { get, post, put, destroy };