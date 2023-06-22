import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListPetsComponent } from './components/list-pets/list-pets.component';
import { PetDetailComponent } from './components/pet-detail/pet-detail.component';
import { LandingComponent } from './components/landing/landing.component';
import { AngularFireAuthGuard, redirectLoggedInTo, redirectUnauthorizedTo } from '@angular/fire/compat/auth-guard'
import { RegisterComponent } from './components/register/register.component';

const redirectUnauthorizedToLogin = () => redirectUnauthorizedTo(['signin']);

const routes: Routes = [
  {path: "listPets", component: ListPetsComponent, canActivate: [AngularFireAuthGuard], data: {authGuardPipe: redirectUnauthorizedToLogin}},
  {path: "petDetails/:id", component: PetDetailComponent, canActivate: [AngularFireAuthGuard], data: {authGuardPipe: redirectUnauthorizedToLogin}},
  {path: "landing", component: LandingComponent},
  {path: "register", component: RegisterComponent}, 
  {path: "signin", loadChildren: ()=> import('./components/signin/signin.module').then(m=>m.SigninModule)},
  {path: '', redirectTo:'listPets', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
