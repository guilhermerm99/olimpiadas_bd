from flask import Flask
from routes.pais_routes import pais_bp
from routes.confederacao_routes import conf_bp
from routes.atleta_routes import atleta_bp
from routes.correlacionar_routes import correlacionar_bp
import threading
import ttkbootstrap as ttk
from tkinter import ttk as tkttk
from tkinter import messagebox, filedialog
from requests import get, post, put, delete
from pandas import DataFrame

app = Flask(__name__)

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

        self.adjust_window_size()

    def select_table(self, table_name):
        self.selected_table = table_name
        self.show_screen2()

    def show_screen2(self):
        self.clear_frame()
        self.current_frame = ttk.Frame(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        label = ttk.Label(self.current_frame, text=f"Tabela: {self.selected_table}\nSelecione uma ação", font=('Helvetica', 18))
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

        if action == "criar" or action == "atualizar":
            if self.selected_table == "País":
                self.build_country_form()
            elif self.selected_table == "Confederação":
                self.build_confederation_form()
            elif self.selected_table == "Atleta":
                self.build_athlete_form()

        action_button = ttk.Button(self.current_frame, text="Executar", command=lambda: self.perform_action(action), bootstyle='primary')
        action_button.pack(pady=10)

        back_button = ttk.Button(self.current_frame, text="Voltar", command=self.show_screen2, bootstyle='secondary')
        back_button.pack(pady=10)


        self.adjust_window_size()

    def create_table(self, df):
        # Criando a Treeview para exibir os dados
        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        tree = tkttk.Treeview(self.table_frame, columns=list(df.columns), show='headings')

        for col in df.columns:
            tree.heading(col, text=col)  
            tree.column(col, anchor='center')

        for index, row in df.iterrows():
            tree.insert('', 'end', values=list(row))  

        tree.pack(expand=True, fill='both')

    def build_country_form(self):
        self.nome_label = ttk.Label(self.current_frame, text="ID do País")
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


    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Selecione a Imagem",
            filetypes=(("Arquivos .avg", "*.avg"), ("Todos os arquivos", "*.*"))
        )
        
        if file_path:
            self.image_path_entry.config(state='normal')
            self.image_path_entry.delete(0, 'end')
            self.image_path_entry.insert(0, file_path)
            self.image_path_entry.config(state='readonly')


    def perform_action(self, action):
        if action == "listar":
            if self.selected_table == 'País':
                response = get(url=f'http://127.0.0.1:5000/api/pais').json()
                response_df = DataFrame(response)
                self.create_table(response_df)
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
                bandeira = self.image_path_entry.get()
                data = {
                    "nome": nome,
                    "sigla": sigla,
                    "bandeira": bandeira
                }
                
                response = post(url='http://127.0.0.1:5000/api/pais', json=data)
                
                if response.status_code == 201:
                    messagebox.showinfo("Sucesso", response.json()["message"])
                else:
                    messagebox.showerror("Erro", "Não foi possível criar o país.")

            elif self.selected_table == "Confederação":
                nome = self.nome_entry.get()
                continente = self.continente_entry.get()
                messagebox.showinfo("Inserir", f"Inserindo Confederação: {nome}, Continente: {continente}")
            elif self.selected_table == "Atleta":
                ano = self.ano_entry.get()
                pais = self.pais_entry.get()
                messagebox.showinfo("Inserir", f"Inserindo Atleta: Ano: {ano}, País: {pais}")
        elif action == "atualizar":
            messagebox.showinfo("Alterar", f"Alterando dados na tabela {self.selected_table}")
        elif action == "deletar":
            messagebox.showinfo("Deletar", f"Deletando dados da tabela {self.selected_table}")

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
