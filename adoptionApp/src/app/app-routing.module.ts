import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListPetsComponent } from './components/list-pets/list-pets.component';
import { PetDetailComponent } from './components/pet-detail/pet-detail.component';
import { LandingComponent } from './components/landing/landing.component';

const routes: Routes = [
  {path: "listPets", component: ListPetsComponent},
  {path: "petDetails/:id", component: PetDetailComponent},
  {path: "landing", component: LandingComponent},
  {path: "signin", loadChildren: ()=> import('./components/signin/signin.module').then(m=>m.SigninModule)},
  {path: '', redirectTo:'listPets', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
