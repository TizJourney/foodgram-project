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
    return this._request(`favorites/${id}/`, 'DELETE', {id});
  }

  getPurchases() {
    return fetch(`${this.apiUrl}/purchases/`, {
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': this.token
      }
    })
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  }
  addPurchases(id) {
    return fetch(`${this.apiUrl}/purchases/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: id
      })
    })
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  }
  removePurchases(id) {
    return fetch(`${this.apiUrl}/purchases/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  }
  addSubscriptions(id) {
    return fetch(`${this.apiUrl}/subscriptions/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: id
      })
    })
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  }
  removeSubscriptions(id) {
    return fetch(`${this.apiUrl}/subscriptions/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  }
  getIngredients(text) {
    return fetch(`${this.apiUrl}/ingredients/?query=${text}`, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  }
}
