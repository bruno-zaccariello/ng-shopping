import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  
  cartAddURL = 'http://localhost:5000/api/carrinho/add/'

  constructor(private http: HttpClient) { }

  addCart(token, pid): Observable<any> {
    let data = {
      'token': token,
      'pid': pid
    }
    return this.http.post<any>(this.cartAddURL, data);
  }
}
