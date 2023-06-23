import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environments } from 'src/environments/environments'
import { Pet } from '../interfaces/pet'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private client:HttpClient) { }

  getAllPets() : Observable<Pet[]>{
    return this.client.get<Pet[]>(environments.apiUrl + "Pet")
  }

  getPetById(id:number) : Observable<Pet> {
    return this.client.get<Pet>(environments.apiUrl + "Pet/GetPetById?id=" + id)
  }
}
