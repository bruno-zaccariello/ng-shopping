import { Component, OnInit, ViewChild } from '@angular/core';
import { ProductService } from '../product.service';
import { CartService } from '../cart.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { LoginComponent } from '../login/login.component';


@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.less']
})
export class ProductComponent implements OnInit {

  public produto;

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private cartService: CartService) { }

  ngOnInit() {
    this.getProduct();
  }

  addCart() {
    // let id = this.produto.id;
    // this.cartService.addCart(this.userTk.userTk, id)
    //   .subscribe(data => this.produto = (data['response']) ? data['produto'] : {});
  }

  getProduct(): void {
    let id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id)
      .subscribe(data => this.produto = (data['response']) ? data['produto'] : {});
  }

}
