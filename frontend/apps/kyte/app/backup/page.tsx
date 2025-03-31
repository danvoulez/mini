'use client'
import axios from 'axios'

export default function BackupPage() {
  const backup = async () => {
    await axios.post('/api/backup')
    alert('Backup criado')
  }

  const restore = async () => {
    await axios.post('/api/backup/restore')
    alert('Restauração feita')
  }

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">Backup e Restauração</h1>
      <button onClick={backup} className="bg-blue-600 text-white px-4 py-2 mr-4 rounded">Criar Backup</button>
      <button onClick={restore} className="bg-green-600 text-white px-4 py-2 rounded">Restaurar Dados</button>
    </main>
  )
}