import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  loginURL = 'http://localhost:5000/api/auth/login'

  constructor(private http: HttpClient) { }

  makeLogin(login,pw): Observable<any> {
    let data = {
      'login': login,
      'senha': pw
    }
    return this.http.post<any>(this.loginURL, data);
  }
}