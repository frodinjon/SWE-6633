import { Component } from '@angular/core';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { from } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'adoptionApp';

  constructor(
    private auth: AuthenticationService,
    private snackBar: MatSnackBar,
    private router: Router
    ){
  }

  logout(){
    return from(this.auth.logout()).subscribe(() => {
    this.router.navigate(['signin']);
    this.snackBar.open("Successfully Logged Out!", "OK", {duration: 5000})})
  }

  
}
