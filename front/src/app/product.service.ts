import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private productsURL = 'http://localhost:5000/api/produtos';
  private productURL = 'http://localhost:5000/api/produtos/'

  constructor(private http: HttpClient) { }

  getProducts(): Observable<any> {
    return this.http.get<any>(this.productsURL);
  }

  getProduct(id: number): Observable<any> {
    let url = this.productURL + id.toString();
    return this.http.get<any>(url);
  }

}
