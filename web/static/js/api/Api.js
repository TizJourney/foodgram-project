
// Это api для интерактивной функционольности сайта
// смотрим приложение api, чтобы узнать идёт обработка запросов на backend'е

class Api {
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
    this.token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
  }
  
  _request(urlTail, method='GET', data=null) {
    const requestParams  = {
      method,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': this.token
      }
    }
    if (data) {
      requestParams ['body'] = JSON.stringify(data);
    }
    return fetch(this.apiUrl + urlTail, requestParams )
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  }

  addFavorites(id) {
    return this._request('favorites/', 'POST', {id});
  }
  removeFavorites(id) {
    return this._request(`favorites/${id}/`, 'DELETE');
  }
  addSubscriptions(id) {
    return this._request('subscriptions/', 'POST', {id});
  }
  removeSubscriptions(id) {
    return this._request(`subscriptions/${id}/`, 'DELETE');
  }
  getIngredients(text) {
    return this._request(`ingredients/?query=${text}`, 'GET');
  }
  getPurchases(id) {
    return this._request('purchases/', 'GET');
  }
  addPurchases(id) {
    return this._request('purchases/', 'POST', {id});
  }
  removePurchases(id) {
    return this._request(`purchases/${id}/`, 'DELETE');
  }
}