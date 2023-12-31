import { Component, OnInit } from '@angular/core';
import {FormControl, Validators, FormGroup, FormBuilder } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {

  form!: FormGroup;
  isLoggingIn = false;
  isRecoveringPassword = false;

  constructor(
    private authenticationService: AuthenticationService,
    private formBuilder: FormBuilder,
    private router: Router,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]]
    });
  }

  login() {
    this.isLoggingIn = true;
    this.authenticationService.signIn({
      email: this.form.value.email,
      password: this.form.value.password
    }).subscribe(() => {
      // this.isLoggingIn = false;
      this.router.navigate(['listPets']);
    }, (error: any) => {
      this.isLoggingIn = false;
      this.snackBar.open(error.message, "OK", {
        duration: 5000
      })
    });
  }

  recoverPassword() {
    this.isRecoveringPassword = true;

    this.authenticationService.recoverPassword(this.form.value.email).subscribe(() => {
      this.isRecoveringPassword = false;
      this.snackBar.open("You can recover your password in your email account.", "OK", {
        duration: 5000
      })
    }, (error: any) => {
      this.isRecoveringPassword = false;
      this.snackBar.open(error.message, "OK", {
        duration: 5000
      })
    })
  }

}
