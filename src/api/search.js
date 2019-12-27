import request from './request'

export function searchHouse(params) {
    return request({
        url: '/house',
        method: 'get',
        params
    })
}