import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.less']
})
export class LoginComponent implements OnInit {

  public userTk = false;

  public login: string;
  public senha: string;

  constructor(
    private loginService: LoginService
  ) { }

  ngOnInit() {
  }

  makeLogin() {
    this.loginService.makeLogin(this.login, this.senha)
      .subscribe(data => this.userTk = (data['response'] && data['login']) ? data['token'] : false);
  }

}
