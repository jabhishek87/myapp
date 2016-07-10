import request from 'reqwest';
import when from 'when';
import {QUOTE_URL} from '../constants/PostConstants';
import QuoteActions from '../actions/Postctions';
import LoginStore from '../stores/LoginStore.js';

class QuoteService {

  nextQuote() {
    request({
      url: QUOTE_URL,
      method: 'GET',
      crossOrigin: true,
      headers: {
        'Authorization': 'Bearer ' + LoginStore.jwt
      }
    })
    .then(function(response) {
      QuoteActions.gotQuote(response);
    });
  }

}

export default new QuoteService()
