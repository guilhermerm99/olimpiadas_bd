from flask import Flask
from routes.pais_routes import pais_bp
from routes.confederacao_routes import conf_bp
from routes.atleta_routes import atleta_bp
from routes.correlacionar_routes import correlacionar_bp
import threading
import ttkbootstrap as ttk
from tkinter import ttk as tkttk
from tkinter import messagebox, filedialog, Toplevel, Label
from requests import get, post, put, delete
from pandas import DataFrame, json_normalize
from PIL import Image, ImageTk
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Registrando as rotas
app.register_blueprint(pais_bp, url_prefix='/api')
app.register_blueprint(conf_bp, url_prefix='/api')
app.register_blueprint(atleta_bp, url_prefix='/api')
app.register_blueprint(correlacionar_bp, url_prefix='/api')

def run_flask():
    app.run(debug=True, use_reloader=False)

# Classe para a Interface Gráfica (Tkinter)
class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.title("CRUD das Olimpíadas")
        self.geometry("400x300")

        self.current_frame = None
        self.selected_table = None  # Tabela selecionada
        self.table_frame = None  # Frame da tabela

        # Iniciar com a primeira tela
        self.show_screen1()

    def show_screen1(self):
        self.clear_frame()
        self.current_frame = ttk.Frame(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        label = ttk.Label(self.current_frame, text="Selecione a tabela", font=('Helvetica', 18))
        label.pack(pady=10)

        country_button = ttk.Button(self.current_frame, text="País", command=lambda: self.select_table("País"), bootstyle='light')
        country_button.pack(pady=5)

        confederation_button = ttk.Button(self.current_frame, text="Confederação", command=lambda: self.select_table("Confederação"), bootstyle='light')
        confederation_button.pack(pady=5)

        athlete_button = ttk.Button(self.current_frame, text="Atleta", command=lambda: self.select_table("Atleta"), bootstyle='light')
        athlete_button.pack(pady=5)

        correlation_button = ttk.Button(self.current_frame, text="Relacionamento", command=self.correlacionar, bootstyle='primary')
        correlation_button.pack(pady=5)

        self.adjust_window_size()

    def select_table(self, table_name):
        self.selected_table = table_name
        self.show_screen2()

    def show_screen2(self):
        self.clear_frame()
        self.current_frame = ttk.Frame(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        label = ttk.Label(self.current_frame, text=f"Tabela: {self.selected_table}\nSelecione uma ação para a tabela", font=('Helvetica', 18))
        label.pack(pady=10)

        read_button = ttk.Button(self.current_frame, text="Listar", command=lambda: self.show_screen3("listar"), bootstyle='light')
        read_button.pack(pady=5)

        insert_button = ttk.Button(self.current_frame, text="Criar", command=lambda: self.show_screen3("criar"), bootstyle='light')
        insert_button.pack(pady=5)

        update_button = ttk.Button(self.current_frame, text="Atualizar", command=lambda: self.show_screen3("atualizar"), bootstyle='light')
        update_button.pack(pady=5)

        delete_button = ttk.Button(self.current_frame, text="Deletar", command=lambda: self.show_screen3("deletar"), bootstyle='danger')
        delete_button.pack(pady=5)

        back_button = ttk.Button(self.current_frame, text="Voltar", command=self.show_screen1, bootstyle='secondary')
        back_button.pack(pady=10)

        self.adjust_window_size()

    def show_screen3(self, action):
        self.clear_frame()
        self.current_frame = ttk.Frame(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        label = ttk.Label(self.current_frame, text=f"Tabela: {self.selected_table}\nAção: {action.capitalize()}", font=('Helvetica', 18))
        label.pack(pady=10)

        if action == "criar":
            if self.selected_table == "País":
                self.build_country_form()
            elif self.selected_table == "Confederação":
                self.build_confederation_form()
            elif self.selected_table == "Atleta":
                self.build_athlete_form()

        elif action == "atualizar":
            if self.selected_table == "País":
                self.update_country()
            if self.selected_table == "Confederação":
                self.update_confederation()
            elif self.selected_table == "Atleta":
                self.update_athlete()

        elif action == "deletar":
            if self.selected_table == "País":
                self.delete_country()
            elif self.selected_table == "Confederação":
                self.delete_confederation()
            elif self.selected_table == "Atleta":
                self.delete_athlete()

        action_button = ttk.Button(self.current_frame, text="Executar", command=lambda: self.perform_action(action), bootstyle='primary')
        action_button.pack(pady=10)

        back_button = ttk.Button(self.current_frame, text="Voltar", command=self.show_screen2, bootstyle='secondary')
        back_button.pack(pady=10)


        self.adjust_window_size()

    def correlacionar(self):
        response = get(url='http://127.0.0.1:5000/api/correlacionar').json()
        self.create_correlation_table(response)

    def create_correlation_table(self, data):
        # Limpa o frame atual e cria um novo frame para a tabela
        self.clear_frame()
        
        # Cria o novo frame para colocar a Treeview
        self.current_frame = ttk.Frame(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Cria a Treeview com as colunas Atleta, Confederação e Sigla do País
        tree = ttk.Treeview(self.current_frame, columns=["Atleta", "Confederação", "Sigla do País"], show="headings")

        # Configura as colunas
        tree.heading("Atleta", text="Atleta")
        tree.heading("Confederação", text="Confederação")
        tree.heading("Sigla do País", text="Sigla do País")

        # Configura o tamanho das colunas
        tree.column("Atleta", anchor='center')
        tree.column("Confederação", anchor='center')
        tree.column("Sigla do País", anchor='center')

        # Insere os dados na tabela
        for item in data:
            tree.insert("", "end", values=(
                item["atleta"]["nome"],
                item["confederacao"]["nome"],
                item["pais"]["sigla"]
            ))

        # Empacota a tabela para que ela seja exibida
        tree.pack(fill="both", expand=True)

        back_button = ttk.Button(self.current_frame, text="Voltar", command=self.show_screen1, bootstyle='secondary')
        back_button.pack(pady=10)
        # Ajusta o tamanho da janela
        self.adjust_window_size()

    def create_table(self, df):
        # Limpa o frame atual e cria um novo frame para a tabela
        self.clear_frame()

        # Cria o novo frame para colocar a Treeview
        self.current_frame = ttk.Frame(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Cria a Treeview com as colunas baseadas no dataframe
        tree = ttk.Treeview(self.current_frame, columns=list(df.columns), show='headings')

        # Configura as colunas
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')

        # Insere os dados na tabela
        for index, row in df.iterrows():
            tree.insert('', 'end', values=list(row))

        # Empacota a tabela para que ela seja exibida
        tree.pack(fill="both", expand=True)

        back_button = ttk.Button(self.current_frame, text="Voltar", command=self.show_screen2, bootstyle='secondary')
        back_button.pack(pady=10)

        self.adjust_window_size()

    def create_table_with_images(self, df):
        self.clear_frame()

        # Criando a Treeview para exibir os dados
        if self.table_frame is not None:
            self.table_frame.destroy()
        
        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        tree = ttk.Treeview(self.table_frame, columns=list(df.columns), show='headings')

        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')

        # Inserindo os dados na Treeview
        for index, row in df.iterrows():
            values = list(row)
            tree.insert('', 'end', values=values)

        tree.pack(expand=True, fill='both')

        # Adicionando as imagens em Labels abaixo da Treeview
        for index, row in df.iterrows():
            image = row['bandeira_image']
            if image:
                bandeira_label = Label(self.table_frame, image=image)
                bandeira_label.image = image  # Necessário para evitar que a imagem seja coletada pelo garbage collector
                bandeira_label.pack()

        back_button = ttk.Button(self.current_frame, text="Voltar", command=self.show_screen2, bootstyle='secondary')
        back_button.pack(pady=10)

        self.adjust_window_size()

    def build_country_form(self):
        self.nome_label = ttk.Label(self.current_frame, text="Nome do País")
        self.nome_label.pack(pady=5)
        self.nome_entry = ttk.Entry(self.current_frame)
        self.nome_entry.pack(pady=5)

        self.sigla_label = ttk.Label(self.current_frame, text="Sigla")
        self.sigla_label.pack(pady=5)
        self.sigla_entry = ttk.Entry(self.current_frame)
        self.sigla_entry.pack(pady=5)

        self.image_label = ttk.Label(self.current_frame, text="Bandeira")
        self.image_label.pack(pady=5)
        self.image_path_entry = ttk.Entry(self.current_frame, state='readonly')
        self.image_path_entry.pack(pady=5)

        self.upload_button = ttk.Button(self.current_frame, text="Selecione a Imagem da Bandeira", command=self.upload_image, bootstyle='light')
        self.upload_button.pack(pady=5)

    def delete_country(self):
        self.id_label = ttk.Label(self.current_frame, text="ID do País")
        self.id_label.pack(pady=5)
        self.id_entry = ttk.Entry(self.current_frame)
        self.id_entry.pack(pady=5)

    def update_country(self):
        self.id_label = ttk.Label(self.current_frame, text="ID do País")
        self.id_label.pack(pady=5)
        self.id_entry = ttk.Entry(self.current_frame)
        self.id_entry.pack(pady=5)

        self.nome_label = ttk.Label(self.current_frame, text="Nome do País")
        self.nome_label.pack(pady=5)
        self.nome_entry = ttk.Entry(self.current_frame)
        self.nome_entry.pack(pady=5)

        self.sigla_label = ttk.Label(self.current_frame, text="Sigla")
        self.sigla_label.pack(pady=5)
        self.sigla_entry = ttk.Entry(self.current_frame)
        self.sigla_entry.pack(pady=5)

        self.image_label = ttk.Label(self.current_frame, text="Bandeira")
        self.image_label.pack(pady=5)
        self.image_path_entry = ttk.Entry(self.current_frame, state='readonly')
        self.image_path_entry.pack(pady=5)

        self.upload_button = ttk.Button(self.current_frame, text="Selecione a Imagem da Bandeira", command=self.upload_image, bootstyle='light')
        self.upload_button.pack(pady=5)

    def build_confederation_form(self):
        # Campos específicos para a tabela Confederação
        self.nome_label = ttk.Label(self.current_frame, text="Nome da Confederação")
        self.nome_label.pack(pady=5)
        self.nome_entry = ttk.Entry(self.current_frame)
        self.nome_entry.pack(pady=5)

        self.pais_label = ttk.Label(self.current_frame, text="ID País")
        self.pais_label.pack(pady=5)
        self.pais_entry = ttk.Entry(self.current_frame)
        self.pais_entry.pack(pady=5)

    def delete_confederation(self):
        self.id_label = ttk.Label(self.current_frame, text="ID da Confederação")
        self.id_label.pack(pady=5)
        self.id_entry = ttk.Entry(self.current_frame)
        self.id_entry.pack(pady=5)

    def update_confederation(self):
        self.id_label = ttk.Label(self.current_frame, text="ID da Confederação")
        self.id_label.pack(pady=5)
        self.id_entry = ttk.Entry(self.current_frame)
        self.id_entry.pack(pady=5)

        self.nome_label = ttk.Label(self.current_frame, text="Nome da Confederação")
        self.nome_label.pack(pady=5)
        self.nome_entry = ttk.Entry(self.current_frame)
        self.nome_entry.pack(pady=5)

        self.pais_label = ttk.Label(self.current_frame, text="ID País")
        self.pais_label.pack(pady=5)
        self.pais_entry = ttk.Entry(self.current_frame)
        self.pais_entry.pack(pady=5)

    def build_athlete_form(self):
        # Campos específicos para a tabela Edição
        self.nome_label = ttk.Label(self.current_frame, text="Nome do Atleta")
        self.nome_label.pack(pady=5)
        self.nome_entry = ttk.Entry(self.current_frame)
        self.nome_entry.pack(pady=5)

        self.genero_label = ttk.Label(self.current_frame, text="Gênero")
        self.genero_label.pack(pady=5)
        self.genero_entry = ttk.Entry(self.current_frame)
        self.genero_entry.pack(pady=5)

        self.data_nasc_label = ttk.Label(self.current_frame, text="Data de Nascimento")
        self.data_nasc_label.pack(pady=5)
        self.data_nasc_entry = ttk.Entry(self.current_frame)
        self.data_nasc_entry.pack(pady=5)

        self.conf_label = ttk.Label(self.current_frame, text="ID Confederação")
        self.conf_label.pack(pady=5)
        self.conf_entry = ttk.Entry(self.current_frame)
        self.conf_entry.pack(pady=5)

        self.modalidade_label = ttk.Label(self.current_frame, text="ID Modalidade")
        self.modalidade_label.pack(pady=5)
        self.modalidade_entry = ttk.Entry(self.current_frame)
        self.modalidade_entry.pack(pady=5)

    def delete_athlete(self):
        self.id_label = ttk.Label(self.current_frame, text="ID do Atleta")
        self.id_label.pack(pady=5)
        self.id_entry = ttk.Entry(self.current_frame)
        self.id_entry.pack(pady=5)

    def update_athlete(self):
        self.id_label = ttk.Label(self.current_frame, text="ID do Atleta")
        self.id_label.pack(pady=5)
        self.id_entry = ttk.Entry(self.current_frame)
        self.id_entry.pack(pady=5)

        self.nome_label = ttk.Label(self.current_frame, text="Nome do Atleta")
        self.nome_label.pack(pady=5)
        self.nome_entry = ttk.Entry(self.current_frame)
        self.nome_entry.pack(pady=5)

        self.genero_label = ttk.Label(self.current_frame, text="Gênero")
        self.genero_label.pack(pady=5)
        self.genero_entry = ttk.Entry(self.current_frame)
        self.genero_entry.pack(pady=5)

        self.data_nasc_label = ttk.Label(self.current_frame, text="Data de Nascimento")
        self.data_nasc_label.pack(pady=5)
        self.data_nasc_entry = ttk.Entry(self.current_frame)
        self.data_nasc_entry.pack(pady=5)

        self.conf_label = ttk.Label(self.current_frame, text="ID Confederação")
        self.conf_label.pack(pady=5)
        self.conf_entry = ttk.Entry(self.current_frame)
        self.conf_entry.pack(pady=5)

        self.modalidade_label = ttk.Label(self.current_frame, text="ID Modalidade")
        self.modalidade_label.pack(pady=5)
        self.modalidade_entry = ttk.Entry(self.current_frame)
        self.modalidade_entry.pack(pady=5)

    def upload_image(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Selecione a Imagem da Bandeira",
                filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg"), ("Todos os arquivos", "*.*")]
            )
            
            if file_path:
                self.image_path_entry.config(state='normal')
                self.image_path_entry.delete(0, 'end')
                self.image_path_entry.insert(0, file_path)
                self.image_path_entry.config(state='readonly') 

        except Exception as e:
            messagebox.showerror("Erro ao carregar imagem", str(e))

    def perform_action(self, action):
        if action == "listar":
            if self.selected_table == 'País':
                # Faz a requisição para listar os países
                response = get('http://127.0.0.1:5000/api/pais').json()
                response_df = DataFrame(response)

                # Lista para armazenar as imagens das bandeiras
                self.bandeira_images = []

                # Itera pelas bandeiras para obter as imagens
                for index, row in response_df.iterrows():
                    bandeira_url = row['bandeira_url']
                    if bandeira_url:
                        bandeira_full_url = f'http://127.0.0.1:5000{bandeira_url}'  # Cria a URL completa
                        # Faz a requisição para obter a imagem
                        bandeira_response = get(bandeira_full_url)
                        if bandeira_response.status_code == 200:
                            # Carrega a imagem
                            image_data = Image.open(BytesIO(bandeira_response.content))
                            # Redimensiona a imagem
                            image_data = image_data.resize((20, 12), Image.LANCZOS)  # Ajuste o tamanho conforme necessário
                            # Converte a imagem para o formato compatível com Tkinter
                            image_tk = ImageTk.PhotoImage(image_data)
                            # Adiciona a imagem à lista de imagens para manter a referência
                            self.bandeira_images.append(image_tk)
                            # Armazena a imagem na nova coluna no DataFrame para exibir na GUI
                            response_df.at[index, 'bandeira_image'] = image_tk
                        else:
                            response_df.at[index, 'bandeira_image'] = None
                    else:
                        response_df.at[index, 'bandeira_image'] = None

                self.create_table_with_images(response_df)

            elif self.selected_table == 'Confederação':
                response = get(url=f'http://127.0.0.1:5000/api/confederacao').json()
                response_df = DataFrame(response)
                self.create_table(response_df)

            elif self.selected_table == 'Atleta':
                response = get(url=f'http://127.0.0.1:5000/api/atleta').json()
                response_df = DataFrame(response)
                self.create_table(response_df)

            self.adjust_window_size()

        elif action == "criar":
            if self.selected_table == "País":
                nome = self.nome_entry.get()
                sigla = self.sigla_entry.get()
                
                bandeira_path = self.image_path_entry.get()
                
                if not bandeira_path:
                    messagebox.showerror("Erro", "Por favor, selecione uma bandeira.")
                    return
                
                with open(bandeira_path, 'rb') as bandeira_file:
                    data = {
                        'nome': nome,
                        'sigla': sigla
                    }
                    
                    files = {
                        'bandeira': bandeira_file
                    }
                    
                    try:
                        response = post(
                            'http://127.0.0.1:5000/api/pais',
                            data=data,
                            files=files
                        )
                        if response.status_code == 201:
                            messagebox.showinfo("Sucesso", f"País {nome} criado com sucesso!")
                        else:
                            messagebox.showerror("Erro", f"Erro ao criar país: {response.json().get('message', 'Erro desconhecido')}")
                    except Exception as e:
                        messagebox.showerror("Erro", f"Erro de conexão: {e}")

            if self.selected_table == "Confederação":
                nome = self.nome_entry.get()
                pais = self.pais_entry.get()

                data = {
                    "nome": nome,
                    "id_pais": pais
                }

                response = post(url='http://127.0.0.1:5000/api/confederacao', json=data)
                
                if response.status_code == 201:
                    messagebox.showinfo("Sucesso", f"Confederação {nome} criada com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível criar a confederação.")

            if self.selected_table == "Atleta":
                nome = self.nome_entry.get()
                genero = self.genero_entry.get()
                data_nasc = self.data_nasc_entry.get()
                id_confederacao = self.conf_entry.get()
                id_modalidade = self.modalidade_entry.get() or None

                data = {
                    "nome": nome,
                    "genero": genero,
                    "data_nasc": data_nasc,
                    "id_confederacao": id_confederacao,
                    "id_modalidade": id_modalidade
                }

                response = post(url='http://127.0.0.1:5000/api/atleta', json=data)
                
                if response.status_code == 201:
                    messagebox.showinfo("Sucesso", f"Atleta {nome} criado com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível criar o atleta.")                

        elif action == "atualizar":
            if self.selected_table == "País":
                id_pais = self.id_entry.get()
                
                nome = self.nome_entry.get()
                sigla = self.sigla_entry.get()
                
                bandeira_path = self.image_path_entry.get()
                
                with open(bandeira_path, 'rb') as bandeira_file:
                    data = {
                        'nome': nome if nome else None,
                        'sigla': sigla if sigla else None
                    }
                    
                    data = {k: v for k, v in data.items() if v is not None}

                    files = {
                        'bandeira': bandeira_file
                    }

                    try:
                        response = put(
                            url=f'http://127.0.0.1:5000/api/pais/{id_pais}', 
                            data=data, 
                            files=files
                        )
                        if response.status_code == 200:
                            messagebox.showinfo("Sucesso", f"País {nome} atualizado com sucesso!")
                        else:
                            messagebox.showerror("Erro", f"Erro ao atualizar país: {response.json().get('message', 'Erro desconhecido')}")
                    except Exception as e:
                        messagebox.showerror("Erro", f"Erro de conexão: {e}")

            if self.selected_table == "Confederação":
                id = self.id_entry.get()
                nome = self.nome_entry.get()
                pais = self.pais_entry.get()

                data = {
                    'nome': nome,
                    'id_pais': pais
                }

                response = put(url=f'http://127.0.0.1:5000/api/confederacao/{id}', json=data)
                
                if response.status_code == 200:
                    messagebox.showinfo("Sucesso", f"Confederação {nome} atualizada com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível atualizar a confederação.")
    
            if self.selected_table == "Atleta":
                id = self.id_entry.get()
                nome = self.nome_entry.get()
                genero = self.genero_entry.get()
                data_nasc = self.data_nasc_entry.get()
                id_confederacao = self.conf_entry.get()
                id_modalidade = self.modalidade_entry.get() 

                data = {
                    'nome': nome if nome else None,
                    'genero': genero if genero else None,
                    'data_nasc': data_nasc if data_nasc else None,
                    'id_confederacao': id_confederacao if id_confederacao else None,
                    'id_modalidade': id_modalidade if id_modalidade else None
                }

                data = {k: v for k, v in data.items() if v is not None}

                response = put(url=f'http://127.0.0.1:5000/api/atleta/{id}', json=data)
                
                if response.status_code == 200:
                    messagebox.showinfo("Sucesso", f"Atleta {nome} atualizado com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível atualizar o atleta.")


        elif action == "deletar":
            if self.selected_table == "País":
                id = self.id_entry.get()

                response = delete(url=f'http://127.0.0.1:5000/api/pais/{id}')
                
                if response.status_code == 200:
                    messagebox.showinfo("Sucesso", "País excluído com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível deletar o país.")


            if self.selected_table == "Confederação":
                id = self.id_entry.get()

                response = delete(url=f'http://127.0.0.1:5000/api/confederacao/{id}')
                
                if response.status_code == 200:
                    messagebox.showinfo("Sucesso", "Confederação excluída com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível deletar a confederação.")

            if self.selected_table == "Atleta":
                id = self.id_entry.get()

                response = delete(url=f'http://127.0.0.1:5000/api/atleta/{id}')
                
                if response.status_code == 200:
                    messagebox.showinfo("Sucesso", "Atleta excluído com sucesso!")
                else:
                    messagebox.showerror("Erro", "Não foi possível deletar o atleta.")

    def clear_frame(self):
        if self.current_frame is not None:
            for widget in self.current_frame.winfo_children():
                widget.destroy()
            self.current_frame.pack_forget()

        if self.table_frame is not None:
            for widget in self.table_frame.winfo_children():
                widget.destroy()
            self.table_frame.pack_forget()

    def adjust_window_size(self):
        self.update_idletasks()
        window_width = self.winfo_reqwidth() + 50
        window_height = self.winfo_reqheight() + 40
        self.geometry(f"{window_width}x{window_height}")

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

app = App()
app.mainloop()
