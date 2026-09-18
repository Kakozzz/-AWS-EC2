from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Usuarios y Libros - UIDE", version="1.0")

# --- ENTIDAD 1: USUARIOS ---
class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

usuarios_db = []

@app.get("/usuarios/", response_model=List[Usuario], summary="Obtener todos los usuarios")
def listar_usuarios():
    return usuarios_db

@app.post("/usuarios/", response_model=Usuario, summary="Crear un usuario")
def crear_usuario(usuario: Usuario):
    for u in usuarios_db:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios_db.append(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}", summary="Eliminar un usuario")
def eliminar_usuario(usuario_id: int):
    for index, u in enumerate(usuarios_db):
        if u.id == usuario_id:
            usuarios_db.pop(index)
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# --- ENTIDAD 2: LIBROS ---
class Libro(BaseModel):
    id: int
    titulo: str
    autor: str

libros_db = []

@app.get("/libros/", response_model=List[Libro], summary="Obtener todos los libros")
def listar_libros():
    return libros_db

@app.post("/libros/", response_model=Libro, summary="Crear un libro")
def crear_libro(libro: Libro):
    for l in libros_db:
        if l.id == libro.id:
            raise HTTPException(status_code=400, detail="El libro ya existe")
    libros_db.append(libro)
    return libro

@app.delete("/libros/{libro_id}", summary="Eliminar un libro")
def eliminar_libro(libro_id: int):
    for index, l in enumerate(libros_db):
        if l.id == libro_id:
            libros_db.pop(index)
            return {"mensaje": "Libro eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")