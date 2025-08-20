import tkinter as tk
from tkinter import messagebox, filedialog

# Lista para armazenar as despesas
despesas = []

def adicionar_despesa():
    descricao = entrada_desc.get()
    valor = entrada_valor.get()

    if not descricao.strip() or not valor.strip():
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    
    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")
        return

    despesas.append((descricao, valor))
    atualizar_lista()
    entrada_desc.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)

def atualizar_lista():
    lista_despesas.delete(0, tk.END)
    total = 0
    for i, (desc, val) in enumerate(despesas):
        lista_despesas.insert(tk.END, f"{desc} - R$ {val:.2f}")
        if i % 2 == 0:
            lista_despesas.itemconfig(i, bg="#3e3c61")
        else:
            lista_despesas.itemconfig(i, bg="#2c2a4a")
        total += val
    label_total.config(text=f"💰 Total gasto: R$ {total:.2f}")

def remover_despesa():
    try:
        indice = lista_despesas.curselection()[0]
        despesas.pop(indice)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma despesa para remover.")

def salvar_txt():
    if not despesas:
        messagebox.showwarning("Aviso", "Nenhuma despesa para salvar.")
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")],
        title="Salvar como"
    )
    if caminho:
        try:
            total = sum(val for _, val in despesas)
            with open(caminho, mode="w", encoding="utf-8") as file:
                file.write("DESPESAS REGISTRADAS\n\n")
                for desc, val in despesas:
                    file.write(f"{desc} - R$ {val:.2f}\n")
                file.write(f"\n💰 Total gasto: R$ {total:.2f}\n")
            messagebox.showinfo("Sucesso", f"Despesas salvas em:\n{caminho}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo:\n{e}")

# ===== INTERFACE =====
janela = tk.Tk()
janela.title("Bufunfa")
janela.geometry("500x680")
janela.config(bg="#2b2a4d")  # Fundo elegante

fonte_titulo = ("Comic Sans MS", 24, "bold")
fonte_normal = ("Arial", 12)
cor_texto = "#FDF6E3"
cor_campo = "#3e3c61"
cor_botao = "#FF6F61"
cor_botao_hover = "#FF4C3B"
cor_botao_remover = "#E74C3C"
cor_botao_remover_hover = "#C0392B"
cor_botao_txt = "#27AE60"
cor_botao_txt_hover = "#1E8449"

def on_enter(e, cor):
    e.widget.config(bg=cor)

def on_leave(e, cor):
    e.widget.config(bg=cor)

# Título
tk.Label(janela, text="Bufunfa", font=fonte_titulo, bg="#2b2a4d", fg="#FFD700").pack(pady=15)

# Campos
tk.Label(janela, text="Descrição:", font=fonte_normal, bg="#2b2a4d", fg=cor_texto).pack()
entrada_desc = tk.Entry(janela, font=fonte_normal, bg=cor_campo, fg=cor_texto,
                        relief="flat", insertbackground="white", width=35)
entrada_desc.pack(pady=5, ipady=4)

tk.Label(janela, text="Valor (R$):", font=fonte_normal, bg="#2b2a4d", fg=cor_texto).pack()
entrada_valor = tk.Entry(janela, font=fonte_normal, bg=cor_campo, fg=cor_texto,
                         relief="flat", insertbackground="white", width=35)
entrada_valor.pack(pady=5, ipady=4)

# Botão adicionar
btn_add = tk.Button(janela, text="Adicionar 💰", font=fonte_normal,
                    bg=cor_botao, fg="white", relief="flat", command=adicionar_despesa)
btn_add.pack(pady=8, ipadx=10, ipady=5)
btn_add.bind("<Enter>", lambda e: on_enter(e, cor_botao_hover))
btn_add.bind("<Leave>", lambda e: on_leave(e, cor_botao))

# Lista
lista_despesas = tk.Listbox(janela, font=fonte_normal, bg=cor_campo, fg=cor_texto,
                            relief="flat", width=45, height=10,
                            selectbackground="#FF6F61", selectforeground="white")
lista_despesas.pack(pady=10)

# Botão remover
btn_remover = tk.Button(janela, text="Remover ❌", font=fonte_normal,
                        bg=cor_botao_remover, fg="white", relief="flat", command=remover_despesa)
btn_remover.pack(pady=5, ipadx=10, ipady=5)
btn_remover.bind("<Enter>", lambda e: on_enter(e, cor_botao_remover_hover))
btn_remover.bind("<Leave>", lambda e: on_leave(e, cor_botao_remover))

# Botão salvar TXT
btn_txt = tk.Button(janela, text="Baixar TXT 📥", font=fonte_normal,
                    bg=cor_botao_txt, fg="white", relief="flat", command=salvar_txt)
btn_txt.pack(pady=5, ipadx=10, ipady=5)
btn_txt.bind("<Enter>", lambda e: on_enter(e, cor_botao_txt_hover))
btn_txt.bind("<Leave>", lambda e: on_leave(e, cor_botao_txt))

# Total
label_total = tk.Label(janela, text="💰 Total gasto: R$ 0.00", font=fonte_normal,
                       bg="#2b2a4d", fg="#FFD700")
label_total.pack(pady=15)

# Direitos autorais (rodapé)
label_rodape = tk.Label(janela, text="© 2025 José Cleison de Lima.",
                        font=("Arial", 9), bg="#2b2a4d", fg="#FDF6E3")
label_rodape.pack(side="bottom", pady=5)

janela.mainloop()
