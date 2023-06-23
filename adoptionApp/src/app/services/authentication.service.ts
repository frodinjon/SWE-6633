import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/compat/auth';
import { Observable, of, from } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(
    private auth: AngularFireAuth
  ) { }

  signIn(params: SignIn): Observable<any>{
    return from(this.auth.signInWithEmailAndPassword(
      params.email, params.password
    ));
  }

  recoverPassword(email: string): Observable<void> {
    return from(this.auth.sendPasswordResetEmail(email))
  }

  registerWithEmailAndPassword(user: {email: string, password: string}) {

    return this.auth.createUserWithEmailAndPassword(user.email, user.password)

  }

  logout(){
    return this.auth.signOut()
  }

  // isLoggedIn(){
  //   console.log(this.auth)
  // }

  

  // isLoggedIn(){

  //   return localStorage.getItem(this.tokenName) != null;

  // }


}

type SignIn = {
  email: string;
  password: string;
}

// recoverPassword(email: string): Observable<void>{
//   return from(this.auth.sendPasswordResetEmail(email))}
