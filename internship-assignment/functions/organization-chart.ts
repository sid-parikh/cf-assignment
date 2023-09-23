interface Env {
    TODO_LIST: KVNamespace;
}
  
export const onRequest: PagesFunction<Env> = async (context) => {
    const task = await context.env.TODO_LIST.get("Task:123");
    return new Response(task);
}
