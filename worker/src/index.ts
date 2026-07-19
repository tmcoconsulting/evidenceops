import { handleRequest } from "./router";
import type { WorkerEnv } from "./env";
import { HttpError, jsonResponse } from "./security";

export default {
  async fetch(request: Request, env: WorkerEnv): Promise<Response> {
    const requestId = crypto.randomUUID();
    const url = new URL(request.url);
    try {
      const response = await handleRequest(request, env);
      const securedResponse = new Response(response.body, response);
      securedResponse.headers.set("X-Request-ID", requestId);
      logEvent(
        requestId,
        request.method,
        url.pathname,
        response.status,
        "request_completed",
      );
      return securedResponse;
    } catch (error) {
      if (error instanceof HttpError) {
        logEvent(
          requestId,
          request.method,
          url.pathname,
          error.status,
          error.code,
        );
        return jsonResponse(
          {
            error: error.code,
            message: error.message,
            human_review_required: true,
          },
          error.status,
          { "X-Request-ID": requestId },
        );
      }
      logEvent(requestId, request.method, url.pathname, 500, "unhandled_error");
      return jsonResponse(
        {
          error: "internal_error",
          message: "EvidenceOps could not complete the request",
          human_review_required: true,
        },
        500,
        { "X-Request-ID": requestId },
      );
    }
  },
} satisfies ExportedHandler<Env>;

function logEvent(
  requestId: string,
  method: string,
  path: string,
  status: number,
  event: string,
): void {
  console.log(
    JSON.stringify({
      event,
      request_id: requestId,
      method,
      path,
      status,
    }),
  );
}
