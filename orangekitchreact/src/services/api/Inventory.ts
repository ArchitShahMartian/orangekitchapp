import { AxiosRequestConfig } from "axios";
import { get } from "./Base.ts";

export const Inventory = {
    list: (params: AxiosRequestConfig) =>
        get('/inventory/get-product-list/', params)
}