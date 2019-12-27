import request from './request'

export function searchHouse(params) {
    return request({
        url: '/house',
        method: 'get',
        params
    })
}

export function searchJob(params) {
    return request({
        url: '/job',
        method: 'get',
        params
    })
}