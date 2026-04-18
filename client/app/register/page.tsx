export default function RegisterPage() {
  return (
    <div className="mx-auto max-w-md card">
      <h1 className="text-2xl font-black text-white">Create your workspace</h1>
      <p className="mt-1 text-sm text-zinc-400">Get started with your first auto-clipping project in minutes.</p>

      <form className="mt-6 space-y-4">
        <label className="block space-y-1">
          <span className="text-sm text-zinc-300">Work email</span>
          <input type="email" className="w-full rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm" placeholder="team@studio.com" />
        </label>
        <label className="block space-y-1">
          <span className="text-sm text-zinc-300">Password</span>
          <input type="password" className="w-full rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm" placeholder="Create a secure password" />
        </label>
        <button type="button" className="w-full rounded-lg bg-indigo-500 px-4 py-2 font-semibold text-white hover:bg-indigo-400">
          Start free plan
        </button>
      </form>
    </div>
  );
}
