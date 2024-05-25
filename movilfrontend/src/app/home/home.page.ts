import { Component } from '@angular/core';
import { HomeService } from './home.service';
import { Person } from './person.model';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  persons: Person[] = [];
  newPerson: Person = { id: 0, nombre: '', apellido: '' };

  constructor(private homeService: HomeService, private alertController: AlertController) {}

  ngOnInit() {
    this.loadPersons();
  }

  loadPersons() {
    this.homeService.getPersons()
      .subscribe(data => {
        this.persons = data;
      });
  }

  async createPerson() {
    const alert = await this.alertController.create({
      header: 'Crear Persona',
      inputs: [
        { name: 'nombre', type: 'text', placeholder: 'Nombre' },
        { name: 'apellido', type: 'text', placeholder: 'Apellido' }
      ],
      buttons: [
        { text: 'Cancelar', role: 'cancel' },
        {
          text: 'Crear',
          handler: data => {
            this.newPerson.nombre = data.nombre;
            this.newPerson.apellido = data.apellido;
            this.homeService.createPerson(this.newPerson)
              .subscribe(() => {
                this.loadPersons();
              });
          }
        }
      ]
    });
    await alert.present();
  }

  async updatePerson(person: Person) {
    const alert = await this.alertController.create({
      header: 'Actualizar Persona',
      inputs: [
        { name: 'nombre', type: 'text', value: person.nombre, placeholder: 'Nombre' },
        { name: 'apellido', type: 'text', value: person.apellido, placeholder: 'Apellido' }
      ],
      buttons: [
        { text: 'Cancelar', role: 'cancel' },
        {
          text: 'Actualizar',
          handler: data => {
            person.nombre = data.nombre;
            person.apellido = data.apellido;
            this.homeService.updatePerson(person.id, person)
              .subscribe(() => {
                this.loadPersons();
              });
          }
        }
      ]
    });
    await alert.present();
  }

  deletePerson(id: number) {
    this.homeService.deletePerson(id)
      .subscribe(() => {
        this.loadPersons();
      });
  }
}
