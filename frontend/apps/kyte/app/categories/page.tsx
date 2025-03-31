'use client'
import useSWR from 'swr'
import axios from 'axios'

export default function Categories() {
  const { data } = useSWR('/api/categories', url => axios.get(url).then(res => res.data))

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">Categorias de Produto</h1>
      <ul className="list-disc pl-5">
        {data?.map((cat: any) => <li key={cat.id}>{cat.name}</li>)}
      </ul>
    </main>
  )
}