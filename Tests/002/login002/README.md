# Leia antes de abrir o arquivo

<div>
<h3>Import pyodbc, Import os and Import mysql.connector</h3>
<p>Você precisará baixar a biblioteca pyodbc, para que os arquivos funcionem.<br>
Você não vai precisar fazer a mesma coisa para o "Import os", porque ele já vem como biblioteca no Python</p>
</div>

## Instalar
<div>
<p>Para Instalar a biblioteca pyodbc:</p>

<h3>No Prompt de Comando</h3>
<code>pip install pyodbc</code>

<h3>No Jupyter</h3>
<code>!pip install pyodbc</code>

<p>Para Instalar a biblioteca mysql.connector:</p>
<h3>No Prompt de Comando</h3>
<code>pip install mysql.connector</code>
</div>

## Banco de Dados MySQL
<div>
<h3>Para criar o banco de dados no MySQL Workbench</h3>
<code>
<var>CREATE DATABASE</var> login;

<var>CREATE TABLE Login</var> (
	ID	<var>INTEGER NOT NULL</var>,
	User	<var>TEXT</var>,
	Password	<var>TEXT</var>,
	<var>PRIMARY KEY</var>(Id)
);</code>
</div>
