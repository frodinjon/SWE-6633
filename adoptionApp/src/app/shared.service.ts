import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://localhost:8000";

  constructor(private http:HttpClient) { }
  
  getAnimalList(): Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/animal/');
  }

  addAnimal(val:any) {
    return this.http.post(this.APIUrl + '/animal/', val);
  }
  updateAnimal(val: any) {
    return this.http.put(this.APIUrl + '/animal/', val);
  }
  deleteAnimal(val: any) {
    return this.http.delete(this.APIUrl + '/animal/'+val);
  }

  getAppUserList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/appUser/');
  }

  addAppUser(val: any) {
    return this.http.post(this.APIUrl + '/appUser/', val);
  }
  updateAppUser(val: any) {
    return this.http.put(this.APIUrl + '/appUser/', val);
  }
  deleteAppUser(val: any) {
    return this.http.delete(this.APIUrl + '/appUser/' + val);
  }
  
  getMessageList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/message/');
  }

  addMessage(val: any) {
    return this.http.post(this.APIUrl + '/message/', val);
  }
  updateMessage(val: any) {
    return this.http.put(this.APIUrl + '/message/', val);
  }
  deleteMessage(val: any) {
    return this.http.delete(this.APIUrl + '/message/' + val);
  }

  getAllAnimalNames(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/animal/');
  }
}
