export default function LoginPage() {
  return (
    <div className="mx-auto max-w-md card">
      <h1 className="text-2xl font-black text-white">Welcome back</h1>
      <p className="mt-1 text-sm text-zinc-400">Sign in to manage uploads, clips, and exports.</p>

      <form className="mt-6 space-y-4">
        <label className="block space-y-1">
          <span className="text-sm text-zinc-300">Email</span>
          <input type="email" className="w-full rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm" placeholder="you@brand.com" />
        </label>
        <label className="block space-y-1">
          <span className="text-sm text-zinc-300">Password</span>
          <input type="password" className="w-full rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm" placeholder="••••••••" />
        </label>
        <button type="button" className="w-full rounded-lg bg-indigo-500 px-4 py-2 font-semibold text-white hover:bg-indigo-400">
          Sign in
        </button>
      </form>
    </div>
  );
}
